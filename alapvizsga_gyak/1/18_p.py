import random

class Pokemon:
    def __init__(self, dex:int, nev:str, ero:float):
        self.nev = nev
        self.dex = dex
        self.ero = ero
    def kepessegvalasztas(self):
        kepessegek = ["parolgas", "tuzhanyas", "loves", "gurulas"]
        self.kepesseg = random.choice(kepessegek)
    
    def beallitas(self):
        self.ugrasimagassag = self.ero * 3 * 0.885

    def csoportositas(self, kor:int):
        if kor >= 15:
            self.csoport = "idos"
        else:
            self.csoport = "fiatal"


pokemonok = []

with open("pokemonLista.txt","r",encoding="utf-8") as f:
    for sor in f:
        adatok = sor.strip().split(",")
        pokemon1=Pokemon(int(adatok[0]),adatok[1],float(adatok[2])) 
        pokemon1.beallitas()
        pokemon1.kepessegvalasztas()
        pokemon1.csoportositas(random.randint(1,50))
        pokemonok.append(pokemon1)
        del pokemon1

with open("pokemonadatok.txt","w",encoding="utf-8") as w:
    for elem in pokemonok:
        w.write(f"Dex: {elem.dex} \n") 
        w.write(f"Név: {elem.nev} \n")
        w.write(f"Erő/Ugrási magasság: {elem.ero}KP/{elem.ugrasimagassag}m \n")
        w.write(f"Képesség / Csoport: {elem.kepesseg} / {elem.csoport} \n")
        w.write(f"*"*30)
        w.write("\n")