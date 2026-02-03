import os
os.system("cls")

def igeny_szamitas(novenyNev:str,nedvTartalom:int):
    vizmennyiseg = 5.0
    if nedvTartalom>60:
        vizmennyiseg = 0.0
    elif nedvTartalom<20:
        if novenyNev.lower() == "pazsit":
            vizmennyiseg = 10.0
        elif novenyNev.lower() == "paradicsom":
            vizmennyiseg = 15.0
    return vizmennyiseg

def naplozas(novenyNev:str,vizMenny:float):
    print(f"Öntözés: {novenyNev} megkapta a {vizMenny} liter vizet.")

novenynev = "kaktusz"
noveny1_vi = igeny_szamitas(novenynev,2)
naplozas(novenynev,noveny1_vi)

novenynev = "bambusz"
noveny2_vi = igeny_szamitas(novenynev,55)
naplozas(novenynev,noveny1_vi)

novenynev = "pálma"
noveny3_vi = igeny_szamitas(novenynev,1)
naplozas(novenynev,noveny1_vi)