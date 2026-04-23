import os
os.system("cls")

try:
    eredetiAr = int(input("Adja meg a termék eredeti árát:  "))
    termekDb = int(input("Adja meg hány db terméket vásárolt:  "))
    kedvezmenySzazalek = float(input("Adja meg mennyi kedvezménye van:  "))

    kedvezmenyesAr = eredetiAr - (eredetiAr * (kedvezmenySzazalek / 100))
    kedvezmenyesAr = round(kedvezmenyesAr,2)

    kedvezmenyesArOsszesen = kedvezmenyesAr * termekDb

    eredetiArOsszesen = eredetiAr * termekDb

    osszesenKedvezmeny = eredetiArOsszesen - kedvezmenyesArOsszesen

    if osszesenKedvezmeny > 20000:
        osszesenKedvezmeny = 20000

    print(f"Egy darab termék kedvezményes ára: {kedvezmenyesAr}")
    print(f"Kedvezményes ár összesen: {kedvezmenyesArOsszesen}")
    print(f"Eredeti ár összesen: {eredetiArOsszesen}")
    print(f"Kedvezmény értéke összesen: {osszesenKedvezmeny}")
except:
    print("Hibás a bevitel")

