import random
class Auto:
    def __init__(self,rendszam:str,futottkm:int,hiba_suly:float):
        self.rendszam = rendszam
        self.futottkm = futottkm
        self.hiba_suly = hiba_suly

    def hasznalat(self,km:int):
        self.futottkm += km

    def szervizdij_szamitas(self):
        self.javitasiktsg = 10000
        if self.futottkm>200000:
            self.javitasiktsg += 5000
        self.javitasiktsg += self.hiba_suly * 2000

    def prioritas_meghatarozas(self):
        if self.hiba_suly >= 8:
            self.prioritas = "SÜRGŐS"
        elif self.hiba_suly>=4 and self.hiba_suly<8:
            self.prioritas = "NORMAL"
        else:
            self.prioritas = "ALACSONY"
    
szerviz_lista = []

with open("autok_x.txt","r",encoding="utf-8") as f:
    for sor in f:
        adatok = sor.strip().split("|")
        auto1 = Auto(adatok[0],int(adatok[1]),float(adatok[2]))
        auto1.hasznalat(random.randint(100,1000))
        auto1.szervizdij_szamitas()
        auto1.prioritas_meghatarozas()
        szerviz_lista.append(auto1)
        del auto1


with open("surgosek.txt","w",encoding="utf-8") as x:
    for auto in szerviz_lista:
        if auto.prioritas == "SÜRGŐS" and auto.javitasiktsg>20000:
            x.write(f"{auto.rendszam}|{auto.javitasiktsg}|{auto.prioritas}\n")


        