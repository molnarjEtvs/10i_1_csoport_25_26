import os
os.system("cls")

szamok = []

for sorszam in range(1,9):
    szam = int(input(f"Add me 8/{sorszam}. számot: "))
    szamok.append(szam)

kilencesekSzama = szamok.count(9)

print(f"9-ek: {kilencesekSzama} db")
