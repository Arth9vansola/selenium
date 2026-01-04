# PostgreSQL Complete Learning Roadmap: Basic to Advanced with Latest Practices

## Executive Summary
This comprehensive guide provides a structured learning path for mastering PostgreSQL, one of the world's most advanced open-source relational database systems. The curriculum spans three progressive phases—Basic, Intermediate, and Advanced—covering foundational SQL commands (DDL, DML, DCL, TCL), intermediate database design, and cutting-edge features like JSONB, window functions, and partitioning. Additionally, this guide includes comparative analysis with MySQL, helping you understand when to choose PostgreSQL over competing RDBMS solutions.

---

## Phase 1: Basic Fundamentals (Foundation Building)
**Duration:** 3-4 weeks | **Target Audience:** Complete beginners to SQL

### 1.1 Installation & Environment Setup
Begin by installing PostgreSQL and supporting tools on your system. PostgreSQL offers platform-specific installers for Windows, macOS, and Linux. During installation, select these components:
- PostgreSQL Server
- pgAdmin 4
- Command-line tools (`psql`, `pg_restore`)

For Linux users, use package managers (apt, yum, brew). For development work, containerization with Docker is recommended.

### 1.2 Core SQL Commands: DDL (Data Definition Language)
DDL commands define and manage database structures.

```sql
CREATE TABLE employees (
    employee_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    salary DECIMAL(10,2),
    department VARCHAR(50),
    hire_date DATE DEFAULT CURRENT_DATE
);

ALTER TABLE employees ADD COLUMN manager_id INTEGER;
ALTER TABLE employees DROP COLUMN manager_id;
ALTER TABLE employees RENAME TO staff;

DROP TABLE employees;
TRUNCATE TABLE employees;
```

Key topics:
- Table creation with constraints (PRIMARY KEY, UNIQUE, NOT NULL, CHECK)
- Data types (INTEGER, VARCHAR, DECIMAL, DATE, TIMESTAMP, BOOLEAN, SERIAL)
- Index creation
- View creation
- Sequences and foreign keys

### 1.3 Core SQL Commands: DML (Data Manipulation Language)
DML commands manipulate the data stored in tables.

```sql
INSERT INTO employees (name, email, salary, department)
VALUES ('John Doe', 'john@company.com', 75000, 'IT');

SELECT * FROM employees;
SELECT name, email, salary FROM employees;

UPDATE employees SET salary = 80000 WHERE name = 'John Doe';

DELETE FROM employees WHERE employee_id = 1;
```

Key topics:
- SELECT with WHERE, ORDER BY, LIMIT
- DISTINCT
- Comparison and logical operators
- NULL handling

### 1.4 Basic Aggregation Functions

```sql
SELECT COUNT(*) FROM employees;
SELECT AVG(salary) AS average_salary FROM employees;

SELECT department, COUNT(*) AS emp_count, AVG(salary) AS avg_salary
FROM employees
GROUP BY department
HAVING COUNT(*) > 2;
```

### 1.5 Learning Resources for Basic Phase
- W3Schools PostgreSQL Tutorial
- PostgreSQL Official Documentation
- DataCamp Beginner's Guide to PostgreSQL
- W3Resource / PGExercises for practice

Recommended steps:
1. Complete basic tutorials
2. Practice with 50+ hands-on queries
3. Build a simple sample database
4. Solve beginner exercises

---

## Phase 2: Intermediate Skills (Database Design & Queries)
**Duration:** 4-5 weeks | **Prerequisite:** Mastery of Phase 1

### 2.1 Advanced SELECT Queries & Joins

```sql
SELECT e.name, d.department_name, e.salary
FROM employees e
INNER JOIN departments d ON e.department_id = d.id;

SELECT e.name, d.department_name
FROM employees e
LEFT JOIN departments d ON e.department_id = d.id;

SELECT e1.name AS employee, e2.name AS manager
FROM employees e1
LEFT JOIN employees e2 ON e1.manager_id = e2.employee_id;
```

Key join types:
- INNER JOIN
- LEFT / RIGHT / FULL JOIN
- SELF JOIN
- Multi-table joins

### 2.2 Subqueries & Common Table Expressions (CTEs)

```sql
SELECT name, salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);

WITH high_earners AS (
    SELECT name, salary, department
    FROM employees
    WHERE salary > 80000
)
SELECT department, COUNT(*) AS count, AVG(salary) AS avg_salary
FROM high_earners
GROUP BY department;

WITH RECURSIVE employee_hierarchy AS (
    SELECT employee_id, name, manager_id, 1 AS level
    FROM employees
    WHERE manager_id IS NULL
    UNION ALL
    SELECT e.employee_id, e.name, e.manager_id, eh.level + 1
    FROM employees e
    INNER JOIN employee_hierarchy eh ON e.manager_id = eh.employee_id
)
SELECT * FROM employee_hierarchy;
```

Use subqueries for simple inline logic; use CTEs for complex or recursive queries.

### 2.3 Transaction Control (TCL) & ACID

```sql
BEGIN;
    UPDATE accounts SET balance = balance - 500 WHERE id = 1;
    UPDATE accounts SET balance = balance + 500 WHERE id = 2;
COMMIT;

BEGIN;
    DELETE FROM employees WHERE department = 'IT';
ROLLBACK;

BEGIN;
    UPDATE table1 SET value = 100;
    SAVEPOINT sp1;
    UPDATE table2 SET value = 200;  -- fails
    ROLLBACK TO sp1;
COMMIT;
```

Isolation levels:

```sql
BEGIN;
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
COMMIT;

BEGIN ISOLATION LEVEL REPEATABLE READ;
COMMIT;

BEGIN ISOLATION LEVEL SERIALIZABLE;
COMMIT;
```

### 2.4 Stored Procedures & Functions

```sql
CREATE FUNCTION get_employee_count() RETURNS INTEGER AS $$
BEGIN
    RETURN (SELECT COUNT(*) FROM employees);
END;
$$ LANGUAGE plpgsql;

CREATE FUNCTION get_salary_by_id(emp_id INTEGER) RETURNS DECIMAL AS $$
DECLARE
    emp_salary DECIMAL;
BEGIN
    SELECT salary INTO emp_salary FROM employees WHERE employee_id = emp_id;
    RETURN emp_salary;
END;
$$ LANGUAGE plpgsql;

CREATE PROCEDURE raise_salaries(department_name VARCHAR, raise_amount DECIMAL) AS $$
BEGIN
    UPDATE employees
    SET salary = salary + raise_amount
    WHERE department = department_name;
    COMMIT;
END;
$$ LANGUAGE plpgsql;

CALL raise_salaries('IT', 5000);
```

### 2.5 Triggers

```sql
CREATE FUNCTION update_employee_modified_time()
RETURNS TRIGGER AS $$
BEGIN
    NEW.modified_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER employees_modified_trigger
BEFORE UPDATE ON employees
FOR EACH ROW
EXECUTE FUNCTION update_employee_modified_time();
```

### 2.6 Views & Materialized Views

```sql
CREATE VIEW high_salary_employees AS
SELECT name, email, salary, department
FROM employees
WHERE salary > 80000
ORDER BY salary DESC;

CREATE MATERIALIZED VIEW monthly_department_stats AS
SELECT department,
       COUNT(*) AS total_employees,
       AVG(salary) AS avg_salary,
       MAX(salary) AS max_salary
FROM employees
GROUP BY department;

REFRESH MATERIALIZED VIEW monthly_department_stats;
```

### 2.7 Data Control Language (DCL)

```sql
CREATE ROLE analyst WITH LOGIN PASSWORD 'secure_password';
GRANT SELECT ON employees TO analyst;
GRANT SELECT, INSERT, UPDATE ON employees TO analyst;

REVOKE INSERT, UPDATE ON employees FROM analyst;

CREATE ROLE hr_manager;
GRANT SELECT, INSERT, UPDATE ON employees TO hr_manager;

CREATE ROLE alice WITH LOGIN;
GRANT hr_manager TO alice;
```

### 2.8 Intermediate Learning Resources
- Coursera: PostgreSQL for Everybody
- edX: PostgreSQL courses
- W3Resource / PGExercises intermediate sets
- Build mid-level projects (e-commerce, school system, social app)

---

## Phase 3: Advanced Mastery (Optimization & Modern Features)
**Duration:** 6-8 weeks | **Prerequisite:** Solid Phase 2 understanding

### 3.1 JSON & JSONB Support

```sql
CREATE TABLE user_profiles (
    user_id BIGSERIAL PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    profile JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO user_profiles (username, profile)
VALUES (
    'john_doe',
    '{"email": "john@example.com", "age": 30, "preferences": {"theme": "dark", "notifications": true}}'::jsonb
);

SELECT username, profile->>'email' AS email FROM user_profiles;
SELECT username, CAST(profile->>'age' AS INTEGER) AS age
FROM user_profiles
WHERE CAST(profile->>'age' AS INTEGER) > 25;

CREATE INDEX idx_profile_gin ON user_profiles USING GIN (profile);
```

Use JSONB for:
- User settings
- Flexible product attributes
- Audit logs and semi-structured data

### 3.2 Window Functions

```sql
SELECT 
    name,
    salary,
    department,
    ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) AS rank
FROM employees;

SELECT 
    order_date,
    amount,
    SUM(amount) OVER (ORDER BY order_date) AS cumulative_sales
FROM orders
ORDER BY order_date;

SELECT 
    order_date,
    amount,
    LAG(amount) OVER (ORDER BY order_date) AS previous_amount,
    amount - LAG(amount) OVER (ORDER BY order_date) AS difference
FROM orders;
```

### 3.3 Advanced Indexing Strategies

```sql
CREATE INDEX idx_employee_email ON employees(email);

CREATE INDEX idx_orders_customer_date
ON orders(customer_id, order_date DESC);

CREATE INDEX idx_active_employees
ON employees(name) WHERE status = 'active';

CREATE INDEX idx_email_lower ON employees(LOWER(email));

CREATE INDEX idx_document_fulltext
ON documents USING GIN(to_tsvector('english', content));

CREATE INDEX idx_tags ON products USING GIN(tags);

CREATE INDEX idx_location ON venues USING GIST(location);

CREATE INDEX idx_timestamps ON logs USING BRIN(created_at);

REINDEX TABLE employees;

EXPLAIN ANALYZE
SELECT * FROM employees WHERE email = 'john@company.com';
```

Best practices:
- Index columns used often in WHERE, JOIN, ORDER BY
- Avoid indexing low-cardinality columns
- Avoid over-indexing write-heavy tables

### 3.4 Query Optimization & Performance Tuning

```sql
EXPLAIN ANALYZE
SELECT e.name, d.department_name, e.salary
FROM employees e
INNER JOIN departments d ON e.department_id = d.id
WHERE e.salary > 70000
ORDER BY e.salary DESC;

-- SELECT only needed columns
SELECT name, email, salary FROM employees;

-- Prefer JOINs over IN subqueries
SELECT o.* FROM orders o
INNER JOIN customers c ON o.customer_id = c.id
WHERE c.status = 'active';

-- Limit results when appropriate
SELECT * FROM events ORDER BY created_at DESC LIMIT 1000;
```

### 3.5 Table Partitioning

```sql
CREATE TABLE orders (
    order_id BIGSERIAL,
    customer_id INTEGER,
    order_date DATE,
    amount DECIMAL(10,2),
    PRIMARY KEY (order_id, order_date)
) PARTITION BY RANGE (order_date);

CREATE TABLE orders_2024_q1 PARTITION OF orders
FOR VALUES FROM ('2024-01-01') TO ('2024-04-01');

CREATE TABLE orders_2024_q2 PARTITION OF orders
FOR VALUES FROM ('2024-04-01') TO ('2024-07-01');

SELECT * FROM orders
WHERE order_date BETWEEN '2024-01-01' AND '2024-03-31';
```

### 3.6 Replication & High Availability (Overview)
- Configure `wal_level`, `max_wal_senders`, `hot_standby`
- Create a replication user
- Use `pg_basebackup` to initialize replicas
- Choose between physical and logical replication

### 3.7 Backup & Recovery

```bash
pg_dump -U postgres -Fc mydb > mydb_backup.sql
pg_restore -U postgres -d mydb mydb_backup.sql

pg_basebackup -D /backup/location -v -P
```

Best practices:
- Regular full backups
- Incremental/WAL-based backups
- Test restore procedures regularly

### 3.8 Row-Level Security (RLS)

```sql
CREATE TABLE salary_data (
    employee_id INTEGER PRIMARY KEY,
    name VARCHAR(255),
    salary DECIMAL(10,2),
    department VARCHAR(50),
    manager_id INTEGER
);

ALTER TABLE salary_data ENABLE ROW LEVEL SECURITY;

CREATE POLICY employee_policy ON salary_data
FOR SELECT TO employee
USING (employee_id = current_user_id);

CREATE POLICY manager_policy ON salary_data
FOR SELECT TO manager
USING (manager_id = current_user_id);
```

### 3.9 Recent/PostgreSQL (2025) Best Practices
- Use JSONB + GIN for semi-structured data
- Use window functions for analytics instead of client-side processing
- Prefer partitioning for massive time-series tables
- Enable monitoring (`pg_stat_statements`, `pg_stat_activity`)
- Use `pgBackRest` or similar for serious backup strategies

---

## MySQL vs PostgreSQL: When to Choose Each

### PostgreSQL Strengths
- Object-relational features and extensibility
- Strong ACID compliance and MVCC
- Advanced indexing (GIN, GiST, BRIN)
- JSONB with indexing
- Full-text search built-in
- Advanced analytics with window functions

### MySQL Strengths
- Simpler and often easier for small projects
- Good read performance
- Wide hosting support
- Familiarity in many dev teams

Choose **PostgreSQL** for:
- Complex data models
- Write-heavy or concurrent workloads
- Applications needing JSONB, full-text search, GIS, custom types

Choose **MySQL** for:
- Simple CRUD applications
- Read-heavy workloads
- Teams already invested in MySQL tooling

---

## SQL Command Categories Summary

### DDL (Data Definition Language)
- Purpose: Define database structure
- Commands: `CREATE`, `ALTER`, `DROP`, `TRUNCATE`, `RENAME`

### DML (Data Manipulation Language)
- Purpose: Manipulate data in tables
- Commands: `SELECT`, `INSERT`, `UPDATE`, `DELETE`

### DCL (Data Control Language)
- Purpose: Manage permissions
- Commands: `GRANT`, `REVOKE`

### TCL (Transaction Control Language)
- Purpose: Control transactions
- Commands: `BEGIN`, `COMMIT`, `ROLLBACK`, `SAVEPOINT`

---

## Structured Learning Timeline (Suggested)

### Month 1 – Basics
- Week 1-2: Installation, DDL fundamentals
- Week 3: DML basics
- Week 4: Aggregates & basic filtering

### Month 2 – Intermediate
- Week 5-6: Joins
- Week 7: Subqueries, CTEs
- Week 8: Transactions & ACID

### Month 3 – Intermediate (Continued)
- Week 9: Functions & procedures
- Week 10: Triggers, views, materialized views
- Week 11-12: DCL & small projects

### Month 4-5 – Advanced
- Week 13-14: JSONB, advanced queries
- Week 15: Window functions
- Week 16: Indexing strategies & tuning

### Month 6-7 – Advanced (Continued)
- Week 17: Partitioning
- Week 18: Replication / backups
- Week 19-20: Security (RLS) & advanced features
- Week 21-24: Capstone projects

---

## Project Ideas by Phase

### Basic Phase Projects
- Personal finance tracker
- Contact manager
- Library catalog

### Intermediate Phase Projects
- E-commerce system
- School management system
- Simple social media platform

### Advanced Phase Projects
- Multi-tenant SaaS with RLS
- Real-time analytics dashboard
- High-throughput logging system with partitioning and indexing

---

## Essential Tools & Extensions
- pgAdmin 4 / DBeaver
- `pg_stat_statements`
- `pg_partman`
- `pgBackRest`
- `pgvector`
- `uuid-ossp`
