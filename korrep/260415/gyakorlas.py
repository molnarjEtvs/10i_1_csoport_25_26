'''szoveg = " skldajflsj ésfsakéja\n"
print(len(szoveg))
ujszoveg = szoveg.strip()
print(len(ujszoveg))
'''
'''
szoveg = "hello,afkls,gdf"
lista = szoveg.split(",")
print(lista[0])
print(lista)
'''
'''
felhasznalok = []
with open("username.csv","r",encoding="utf-8") as f:
    for sor in f:
        adat = sor.strip().split(";")
        felhasznalo = {}
        felhasznalo['nev'] = adat[0]
        felhasznalo['az'] = adat[1]
        felhasznalok.append(felhasznalo)

with open("szurt.txt","w",encoding="utf-8") as a:
    for felhasznalo in felhasznalok:
        a.write(f"{felhasznalo['nev']}:{felhasznalo['az']}\n")

'''

felhasznalok = []
with open("pw.csv","r",encoding="utf-8") as f:
    for sor in f:
        adat = sor.strip().split(";")
        if adat[7] == "Manchester":
            felhasznalo = {}
            felhasznalo['keresztnev'] = adat[4]
            felhasznalo['vezeteknev'] = adat[5]
            felhasznalok.append(felhasznalo)

with open("manchesteriek.txt","w",encoding="utf-8") as a:
    for felh in felhasznalok:
        a.write(f"{felh['vezeteknev']} {felh['keresztnev']}\n")