import random
class Szallashely:
    def __init__(self,nev:str,ar:float,helyek:int):
        self.nev = nev
        self.ar = ar
        self.helyek = helyek
    
    def helyFrissites(self,db:int):
        self.helyek += db
        if self.helyek>21:
            self.helyek = 21

    def kedvezmenyGeneralas(self):
        szamok = [5,10,20,30]
        self.kedvezmeny = random.choice(szamok)
        self.kedvezmenyesAr = self.ar*(100-self.kedvezmeny)/100
        self.kedvezmenyesAr = round(self.kedvezmenyesAr,3)

szallasok = []


with open("szallasok.txt","r",encoding="utf-8") as f:
    for sor in f:
        adatok = sor.strip().split("|")
        szallas1 = Szallashely(adatok[0],float(adatok[1]),int(adatok[2]))
        szallas1.helyFrissites(random.randint(1,21))
        szallas1.kedvezmenyGeneralas()
        szallasok.append(szallas1)
        del szallas1


with open("akciosszallasok.txt","w",encoding="utf-8") as d:
    for egySzallas in szallasok:
        if egySzallas.kedvezmeny<=10:
            d.write(f"Szállás neve: {egySzallas.nev}\n")
            d.write(f"Ár/éjszaka/fő: {egySzallas.ar} Ft\n")
            d.write(f"Kedvezmény mértéke: {egySzallas.kedvezmeny}%\n")
            d.write(f"Kedvezményes éjszaka ára: {egySzallas.kedvezmenyesAr} Ft\n")
            d.write(f"Szabad helyek száma: {egySzallas.helyek} db\n")
            d.write("#"*30)
            d.write("\n")
    