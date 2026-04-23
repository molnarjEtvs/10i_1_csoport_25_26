import os, math
os.system("cls")

try:
    sugar = int(input("Add meg a sugárt: "))
    magassag = int(input("Add meg a magasságot: "))
except:
    print("Hibás adatbevitel")

pi = 3.14
a = math.sqrt(sugar**2 + magassag**2)
A = (sugar**2 * pi + sugar * pi * a)
V = ((sugar**2 * pi * magassag)/3)
A = round(A,2)
V = round(V,2)
print(f"A térfogat: {V}")
print(f"A felszín: {A}")
if A >= 10:
    print("A felszín legalább 10.")