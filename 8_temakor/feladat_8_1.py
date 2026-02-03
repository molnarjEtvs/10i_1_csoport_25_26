import os
os.system("cls")


def fizetes_szamitas(oraszam:int,oraber:float,tuloraSzorzo:float = 1.5):
    fizetes = 0
    if oraszam<=40:
        fizetes = oraszam*oraber
    else:
        alap = oraber * 40
        tulora = (oraszam-40)*(oraber*tuloraSzorzo)
        fizetes = alap+tulora
    return fizetes

eset1 = fizetes_szamitas(35,2000)
print(f"{eset1} Ft")

eset2 = fizetes_szamitas(45,2000)
print(f"{eset2} Ft")

eset3 = fizetes_szamitas(42,2000,2.0)
print(f"{eset3} Ft")