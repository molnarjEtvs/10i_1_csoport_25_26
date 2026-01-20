import os,random
os.system("cls")
lehetosegek = ["K","P","O"]

nyeresekDb = 0
vesztesekDb = 0
dontetlenDb = 0

for _ in range(5):
    
    user = input("Kő (K), Papír (P), Olló (O): ").upper()
    gep = random.choice(lehetosegek)
    os.system("cls")
    print(f"Gép: {gep} | User: {user}")
    if user == gep:
        print("Döntetlen!")
        dontetlenDb += 1
    elif (user == "P" and gep == "K") or (user == "K" and gep == "O") or (user == "O" and gep == "P"):
        print("Nyertél!")
        nyeresekDb += 1
    else:
        print("Vesztettél!")
        vesztesekDb += 1
    

print(f'Nyerések száma: {nyeresekDb} db ')
print(f'Vesztések száma: {vesztesekDb} db ')
print(f'Döntetlenek száma: {dontetlenDb} db ')
