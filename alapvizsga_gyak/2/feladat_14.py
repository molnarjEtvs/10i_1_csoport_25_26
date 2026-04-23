
def orszagRogzites():
    orszagok = []
    while True:
        orszag = input("add meg az országot: ").capitalize()
        if not orszag:
            break
        orszagok.append(orszag)
    return orszagok

def orszagStatisztika(orszagok:list):
    db = len(orszagok)
    print(f"{db} db ország került rögzítésre")
    lsDb = 0
    for orszag in orszagok:
        if orszag.find('s')>-1 and orszag.find('l')>-1:
            lsDb += 1
    print(f"ls -es: {lsDb} db")
    szoveg = "-".join(orszagok)
    print(f"{orszagok}")

n = orszagRogzites()
orszagStatisztika(n)
