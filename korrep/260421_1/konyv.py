
def konyvRogzites():
    konyvek = []
    while True:
        konyvCim = input("Adj meg címet: ").capitalize()
        if not konyvCim:
            break
        konyvek.append(konyvCim)
    return konyvek

def konyvElemzes(konyvek:list):
    db = len(konyvek)
    print(f"{db} db könyv került rögzítése")
    bdb = 0
    for konyv in konyvek:
        if konyv.find("b")>-1:
            bdb += 1
    print(f"{bdb} db b betűs van")
    utolsoElotti = konyvek[-2]
    print(f"Utolsó előtti: {utolsoElotti}")
    azElemek = []
    for konyv in konyvek:
        if konyv.startswith("A") == True and konyv.endswith("z") == True:
            azElemek.append(konyv)
    szoveg = ",".join(azElemek)
    print(f"{szoveg}")

s = konyvRogzites()
konyvElemzes(s)