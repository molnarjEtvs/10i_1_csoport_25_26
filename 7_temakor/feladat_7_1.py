import os
os.system("cls")

telefonszamok = []

while True:
    nev = input("Add meg a nevet: ")
    if nev.upper() == "VÉGE":
        break
    tel = input("Telefonszám: ")
    telefonszam = {}
    telefonszam['nev'] = nev
    telefonszam['tel'] = tel
    telefonszamok.append(telefonszam)

keresett = input("add meg kit keresel: ")
talalat = ""
for tember in telefonszamok:
    if tember['nev'] == keresett:
        talalat = tember

if talalat == "":
    print("Nincs ilyen ember/telefonszám")
else:
    print(talalat['tel'])