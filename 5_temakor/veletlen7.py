import os, random
os.system("cls")

bekert = int(input("Adj meg egy számot 10-1000: "))
rszam = random.randint(10,1000)

print(f"Random szám: {rszam}, bekért: {bekert}")
if bekert>rszam:
    print("A bekért szám nagyobb")
elif bekert<rszam:
    print("A random szám nagyobb")
else:
    print("Egyenlő")