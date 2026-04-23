import random
class Film:
    def __init__(self,azon:str,cim:str,ev:int,dij:int,jelol:int):
        self.azon = azon
        self.cim = cim
        self.ev = ev
        self.dij = dij
        self.jelol = jelol

    def szamolas(self):
        self.elteltIdo = 2026 - self.ev

    def bevetelGeneralas(self):
        self.bevetel = random.randint(1000000,10000000)

filmek = []

with open("oscar.csv","r",encoding="utf-8") as f:
    for sor in f:
        adatok = sor.strip().split(";")
        film1 = Film(adatok[0],adatok[1],int(adatok[2]),int(adatok[3]),int(adatok[4]))
        film1.szamolas()
        film1.bevetelGeneralas()
        filmek.append(film1)
        del film1


with open("filmadatok.txt","w",encoding="utf-8") as i:
    for film in filmek:
        if film.bevetel >= 5000000:
            i.write(f"{film.cim}\n")
            i.write(f"{film.bevetel} euro\n")
            i.write(f"{film.elteltIdo}\n")
            i.write("-"*20)
            i.write("\n")
        
