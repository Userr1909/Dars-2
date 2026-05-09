# 6-masala. List va String ma'lumotlarini berilgan. Listdagi barcha elementlarning boshiga berilgan stringni qo'shib qo'ying.
# Input:list: [1,2,3,4], string: emp
# Output: ['emp1', 'emp2', 'emp3', 'emp4']
import os
os.system ("cls")

lst = [1, 2, 3, 4]
string = 'emp'
list1 = []

for i in lst:
    yangi_element = string + str(i)
    list1.append(yangi_element)

print(list1)
# tayyor