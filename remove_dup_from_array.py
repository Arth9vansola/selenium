list1 = [3,3,5,7,7,7,7,9,9,9,12,12]
list2 = []

for lst in list1:
  if lst not in list2:
    list2.append(lst)

list1.clear()
list1 = list2
print(list1)
