import os,math
os.system("cls")

try:
    koncentratum = int(input("Add meg a koncentrátumot: "))
    homerseklet = float(input("Add meg a hőmérsékletet: "))
    szerencsFaktor = 1.25

    stabIdo = math.sqrt((koncentratum+homerseklet)*szerencsFaktor)
    stabIdo = round(stabIdo,2)

    if stabIdo<10:
        print(f"Instabil főzet....")
    elif stabIdo>=10 and stabIdo<35:
        print("Tökéletes időzítés...")
    else:
        print("Túlfőzött lötty!...")
except:
    print("Hiba:csak számokat használj a kotyvasztáshoz!")
