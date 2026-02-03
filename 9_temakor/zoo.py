import os
os.system("cls")

allatok = []
with open("allatok.txt","r",encoding="utf-8") as f:
    for sor in f:
        adatok = sor.strip().split(";")
        allat = {}
        allat['nev'] = adatok[0]
        allat['faj'] = adatok[1]
        allat['suly'] = float(adatok[2])
        allat['kor'] = int(adatok[3])
        allatok.append(allat)

db = len(allatok)
print(f"állatok száma: {db} db")

db_oroszlan = 0
for allat in allatok:
    if allat['faj'] == "Oroszlán":
        db_oroszlan += 1
print(f"orszolánok száma: {db_oroszlan} db")

legAllat = allatok[0]
for allat in allatok:
    if allat['suly']>legAllat['suly']:
        legAllat = allat
print(f"A legnehezebb állat: {legAllat['nev']}")

with open("nyugdijasok.txt","w",encoding="utf-8") as i:
    for allat in allatok:
        if allat['kor']>15:
            i.write(f"{allat['nev']};{allat['faj']}\n")

