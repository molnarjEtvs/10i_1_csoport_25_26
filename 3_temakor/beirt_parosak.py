import os
os.system("cls")

parosDb = 0

while True:
    szam = int(input("Add meg a számot: "))
    if szam==0:
        break
    if szam%2 == 0:
        parosDb +=1

print(f"Páros számok: {parosDb}")