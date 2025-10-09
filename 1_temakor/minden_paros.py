import os
os.system("cls")

szam1 = int(input("Add meg az 1 számot: "))
szam2 = int(input("Add meg az 2 számot: "))
szam3 = int(input("Add meg az 3 számot: "))

if szam1%2==0 and szam2%2==0 and szam3%2==0:
    print(f"A beírt három szám: {szam1}, {szam2}, {szam3} mindegyik PÁROS!")
else:
    print("A beírt számok valamelyike nem páros!")

    