import os
os.system("cls")

mondat = input("Adj meg egy mondatot: ")
betuk = {}
for betu in mondat:
    if betu not in betuk:
        betuk[betu] = 1
    else:
        betuk[betu] += 1


'''
h:1db
2:2db
'''
for betu,darab in betuk.items():
    print(f"{betu}:{darab} db")