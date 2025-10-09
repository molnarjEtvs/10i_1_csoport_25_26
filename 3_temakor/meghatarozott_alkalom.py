import os
os.system("cls")

db = int(input("Add meg hányszor írjam ki: "))
szo = input("Add meg a szót: ")

for sorszam in range(1,db+1):
    print(f"{sorszam}. {szo}")