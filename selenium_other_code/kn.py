# people = ["Avi", "Rahul", "Neha"]

# for index, name in enumerate(people, start=1):
#     print(index, name)
from itertools import chain
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# merged_list = [*list1, *list2]

# merged_list = list(chain(list1, list2))

# print(merged_list)

merged = [item for pair in zip(list1, list2) for item in pair]
print(merged)
