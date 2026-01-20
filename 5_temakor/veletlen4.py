import os, random
os.system("cls")

szamok = []
db = int(input("Add meg hány db véletlen számot szeretnél: "))
tol = int(input("Add meg a kezdő számot: "))
veg = int(input("Add meg a vég értéket:"))

for _ in range(db):
    vszam = random.randint(tol,veg)
    szamok.append(vszam)

print(szamok)