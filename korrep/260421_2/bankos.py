import random
class BankSzamla:
    def __init__(self,nev:str,egyenleg:int):
        self.nev = nev
        self.egyenleg = egyenleg
        self.dij = 0

    def befizetes(self,osszeg:int):
        self.egyenleg += osszeg
        self.dij -= 10
        if self.dij < 0:
            self.dij = 0

    def kivetel(self,osszeg:int):
        if self.egyenleg >= osszeg:
            self.egyenleg -= osszeg
            self.dij += round(osszeg * 0.85,2)
            return True
        else:
            return False
    

szamlak = []

with open("bankszamlak.txt","r",encoding="utf-8") as f:
    for sor in f:
        adatok = sor.strip().split(";")
        bszamla1 = BankSzamla(adatok[0],int(adatok[1]))
        bszamla1.befizetes(random.randint(1000,10000))
        for _ in range(3):
            bszamla1.kivetel(random.randint(1000,3000))
        szamlak.append(bszamla1)
        del bszamla1

with open("disneySzamlak.txt","w",encoding="utf-8") as x:
    for szamla in szamlak:
        if szamla.egyenleg > 20000:
            x.write(f"Ügyfél neve: {szamla.nev}\n")
            x.write(f"Egyenleg: {szamla.egyenleg}\n")
            x.write(f"Számlavezetési díj: {szamla.dij}\n")
            x.write("#"*30)
            x.write("\n")