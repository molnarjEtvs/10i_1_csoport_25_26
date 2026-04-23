class Szamitogep:
    def __init__(self,processzorSeb:float,alaplapTipus:str,ramMeret:int):
        self.processzorSeb = processzorSeb
        self.alalapTipus = alaplapTipus
        self.ramMeret = ramMeret
        print("megszületett a számítógép")

    def ramBovites(self,ramMeret:int):
        self.ramMeret += ramMeret


meret = input("add meg a processzor sebességet: ")

szamitogep1 = Szamitogep(float(meret),"Asus",32)
szamitogep1.ramBovites(10)
szamitogep1.ramBovites(2)

szamitogep2 = Szamitogep(5.0,"Asus",8)
szamitogep2.ramBovites(16)


