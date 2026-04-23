import random
class Auto:
    def __init__(self,rendszam:str,futtot_km:int,hiba_suly:float):
        self.rendszam = rendszam
        self.futott_km = futtot_km
        self.hiba_suly = hiba_suly
    
    def hasznalat(self,km:int):
        self.futott_km += km
    
    def szerviz_dij_szamitas(self):
        self.javitasiktsg = 10000
        self.javitasiktsg += self.hiba_suly * 2000
        if self.futott_km>200000:
            self.javitasiktsg += 5000

    def prioritas_meghatarozas(self):
        if self.hiba_suly>=8:
            self.prioritas = "SÜRGŐS"
        elif self.hiba_suly>4 and self.hiba_suly<=7.9:
            self.prioritas = "NORMÁL"
        else:
            self.prioritas = "ALACSONY"
    
szerviz_lista = []

with open("autok_x.txt","r",encoding="utf-8") as f:
    for sor in f:
        adatok = sor.strip().split("|")
        auto1 = Auto(adatok[0],int(adatok[1]),float(adatok[2]))
        auto1.hasznalat(random.randint(100,1000))
        auto1.szerviz_dij_szamitas()
        auto1.prioritas_meghatarozas()
        szerviz_lista.append(auto1)
        del auto1


with open("prioritasok.txt","w",encoding="utf-8") as k:
    for auto in szerviz_lista:
        if auto.prioritas == "SÜRGŐS" and auto.javitasiktsg>20000:
            k.write(f"{auto.rendszam} | {auto.javitasiktsg} | {auto.prioritas}\n")
