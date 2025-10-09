import os
os.system("cls")

szam = int(input("Adj meg egy számot: "))
if szam%3 == 0:
    print(f"A {szam} oszható 3-al")
else:
    print(f"A {szam} NEM osztható 3-algit")