import os, random
os.system("cls")

gondolt_szam = random.randint(1,1000)
sorszam=1
while True:
    tipp = int(input(f"Add meg a(z){sorszam}. tipped: "))
    sorszam+=1
    if tipp==gondolt_szam:
        print("Gratulálok nyertél!")
        break
    elif gondolt_szam>tipp:
        print("A gondolt szám nagyobb!")
    else:
        print("A gondolt szám kisebb!")