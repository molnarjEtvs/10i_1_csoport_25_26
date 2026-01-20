import os, random
os.system("cls")

tipus = input("Egész vagy lebegőpontos számot szeretnél? (L: lebegő, E: egész): ")

if tipus == "L":
    szam = random.uniform(8,88)
elif tipus == "E":
    szam = random.randint(8,88)
else:
    szam = "Nem ismer ilyen típust"

print(szam)