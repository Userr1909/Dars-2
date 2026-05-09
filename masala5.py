# 5-masala. Sonlardan iborat listlarni o'zida saqlaydigan list berilgan. Ichki listlarning elementlar yig'indisi eng katta bo'lgan listni toping.
# Input: [ [1,2,3], [4,5,6], [10,11,12], [7,8,9] ]
# Output: [10, 11, 12]
import os
os.system ("cls")

list1 = [ [1,2,3], [4,5,6], [10,11,12], [7,8,9] ]

engkatta = 0
natija = 0

for i in list1:
    yigindi = 0
    for j in i:
        yigindi += j
    if yigindi > engkatta:
        engkatta=yigindi
        natija = i
print(natija)
# tayyor