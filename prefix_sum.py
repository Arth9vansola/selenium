# 1st solution where i return newly created list
# list1 = [3,1,8,2,10,5]
# n = len(list1)
# sum = []
# sum.append(list1[0])
# for i in range(1, n):
#   x = sum[i-1] + list1[i]
#   sum.append(x)
  
# print(sum)  

# 2nd solution where i return the original list without creating new list like sum
list1 = [3,1,8,2,10,5]
n = len(list1)
for i in range(1, n):
  list1[i] += list1[i-1]
print(list1) 