import os
os.system("cls")

nevek = []
while True:
    nev = input("Adj meg egy nevet: ")
    #if nev == "":
    if not nev:
        break
    nevek.append(nev)

print(nevek)