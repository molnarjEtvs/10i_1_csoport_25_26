import os
os.system("cls")

nevek = []

while True:
    nev = input("Adj meg egy nevet: ")
    #if not nev:
    if nev == "":
        break
    nevek.append(nev)

print(f"{nevek[0]}")
print(f"{nevek[-1]}")