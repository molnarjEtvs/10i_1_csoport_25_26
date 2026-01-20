import os
os.system("cls")

csunyak = ["fasz","kurva","geci"]
szepek  = ["pénisz","prostitualt","Sperma"]

mondat = input("Adj meg egy csúnya mondatot: ")

for x in range(len(csunyak)):
    mondat = mondat.replace(csunyak[x],szepek[x])

print(mondat)