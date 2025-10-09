import os
os.system("cls")

szam = int(input("Adj meg egy egész számot: "))
if szam%2 == 0:
    print(f"A {szam} páros!")
else:
    print(f"A {szam} páratlan!")