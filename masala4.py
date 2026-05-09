# 4-masala. Input orqali kiritilgan string ma'lumotlarni tuplega bittalab(har bir belgisini) joylashtiring.
# Input: python 3.0
# Output: ('p', 'y', 't', 'h', 'o', 'n', '3', '.', '0')
import os
os.system ("cls")

string = input()
# list = []
sonlar = ()

for i in string:
    if i != " ":
        # list.append(i)
        sonlar = sonlar + (i,)

# sonlar = tuple(list)
print(sonlar)
# tayyor
