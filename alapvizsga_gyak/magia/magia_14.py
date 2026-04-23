
def atkok_kezeles():
    atkok = []
    while True:
        atok = input("adj meg egy átkot: ").upper()
        if not atok:
            break
        atkok.append(atok)
    return atkok

def atkokElemzes(atkok:list):
    
    db = len(atkok)
    print(f"{db} db átok lett rögzítve")
    
    dbs = 0
    for atok in atkok:
        if atok.startswith("S") == True and atok.endswith("S") == True:
            dbs += 1
    print(f"s betűsek száma: {dbs} db")
    
    szoveg = "<\>".join(atkok)
    print(f"{szoveg}")

a = atkok_kezeles()
atkokElemzes(a)