class Macska:

    def __init__(self,nev:str,suly:float,ehes:bool):
        self.nev = nev
        self.suly = suly
        self.ehes = ehes
    
    def eszik(self,etelMennyiseg:float):
        if self.ehes == True:
            self.suly += etelMennyiseg
            self.ehes = False
            return True
        else:
            return False
    
    def futkos(self):
        self.suly -= 0.1
        if self.ehes == False:
            self.ehes = True

    def jelenlegiErtekek(self):
        print(f"Név: {self.nev}")
        print(f"Súly: {self.suly} kg")
        if self.ehes == True:
            print(f"{self.nev} ÉHES")
        else:
            print(f"{self.nev} NEM éhes")

macska1 = Macska("István",4.2,True)
if macska1.eszik(0.3) == True:
    print(f"{macska1.nev} evett")
else:
    print(f"{macska1.nev} NEM evett")
macska1.futkos()
macska1.jelenlegiErtekek()

macska2 = Macska("Ferenc",13.4,False)
if macska2.eszik(1.3) == True:
    print(f"{macska2.nev} evett")
else:
    print(f"{macska2.nev} NEM evett")
macska2.futkos()
macska2.jelenlegiErtekek()