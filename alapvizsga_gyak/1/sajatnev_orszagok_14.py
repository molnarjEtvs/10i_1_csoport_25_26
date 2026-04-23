import os
os.system('cls')
#csak akkor van self ha van class is!!!
def orszagRogzites():
    orszagok = []
    while True:
        orszagnev = input("Add meg az ország nevét: ").capitalize()
        if not orszagnev:
            break
            
        orszagok.append(orszagnev)

    
    return orszagok

def orszagStatisztika(orszagok:list):
    db = len(orszagok)
    print(f"{db} ország lett rögzítve")
    sldb = 0
    for orszag in orszagok:
        if orszag.find("s") >-1 and orszag.find("l") >-1:
            sldb += 1
        
        print(f"S és L betűs országok: {sldb} db van")

