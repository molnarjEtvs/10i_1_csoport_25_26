import os, random
os.system("cls")

szamok = []
db = int(input("Add meg hány db véletlen számot szeretnél: "))

for _ in range(db):
    vszam = random.randint(100,1000)
    szamok.append(vszam)

print(szamok)