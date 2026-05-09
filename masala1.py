# 1-masala. a dan b sonigacha juft sonlarlarni to'g'ri tartibda listga joylashtirish. a va b input orqali olinsin.
# Input: a=10 b=20
# Output: sonlar=[10,12,14,16,18]
import os
os.system ("cls")

a = int(input("A = "))
b = int(input("b = "))
sonlar = []

for i in range(a,b):
    if i % 2 == 0:
        sonlar.append(i)
print(sonlar)
# tayyor