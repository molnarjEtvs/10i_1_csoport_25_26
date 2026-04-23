import os
os.system("cls")

def vizsgaAllpot(pontszam:int):
    if pontszam>=48:
        return True
    else:
        return False
    
while True:
    nev = input("Add meg a nevet: ")
    if not nev:
        break
    pont = int(input("Add meg a pontszámot: "))
    if vizsgaAllpot(pont) == True:
        print(f"{nev} SIKERES vizsgát tett")
    else:
        print(f"{nev} SIKERTELEN vizsgát tett.")