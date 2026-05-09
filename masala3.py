# 3-masala. List ichida tuplelar berilgan va ushbu tuplelarning oxirgi elementini 100 bilan almashtiring.
# Input: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]
import os
os.system ("cls")

list1 = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
list2 = []

for i in list1:
    tuple1 = (i[0],i[1],100)
    list2.append(tuple1)
print(list2)
# tayyor