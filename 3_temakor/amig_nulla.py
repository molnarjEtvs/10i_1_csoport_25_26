import os
os.system("cls")

osszeg = 0

#1. megoldás
while True:
    szam = int(input("Adj meg egy számot: "))
    if szam == 0:
        break
    osszeg += szam
print(f"Összeg: {osszeg}")

#2.megoldás

osszeg = 0
szam = 1
while szam != 0:
    szam = int(input("Adj meg egy számot: "))
    osszeg += szam
print(f"Összeg: {osszeg}")