import os,random
os.system("cls")

versenyzok = []
while True:
    nev = input("Add meg a nevet: ")
    if nev.lower() == "kész":
        break
    rajtszam = int(input("Add meg a rajtszámot: "))
    atlagSeb = random.uniform(8,18)
    versenyzo = {}
    versenyzo['nev'] = nev
    versenyzo['rajtszam'] = rajtszam
    versenyzo['atlagSeb'] = atlagSeb
    versenyzok.append(versenyzo)

print(versenyzok)
