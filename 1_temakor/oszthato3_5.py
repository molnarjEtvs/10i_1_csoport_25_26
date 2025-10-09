import os
os.system("cls")

szam = int(input("Adj meg egy számot: "))
if szam%3==0 and szam%5==0:
    print(f"A {szam} 3-al és 5-el is osztható")
elif szam%3==0:
    print(f"A {szam} 3-al osztható")
elif szam%5==0:
    print(f"A {szam} 5-al osztható")
else:
    print(f"A {szam} egyikkel sem osztható")