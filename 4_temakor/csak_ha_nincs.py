import os
os.system("cls")

szamok = []

while True:
    szam = float(input("Adj meg egy lebegőpontos számot: "))
    if szam == 0:
        break
    if szam not in szamok:
        szamok.append(szam)

print(szamok)