import os, random
os.system("cls")

kettesek = []
harmasok = []
otosok = []

for _ in range(30):
    vszam = random.randint(300,1500)
    if vszam%2==0:
        kettesek.append(vszam)
    if vszam%3==0:
        harmasok.append(vszam)
    if vszam%5==0:
        otosok.append(vszam)

print(f"Kettesek:\n {kettesek}")
print(f"Harmasok:\n {harmasok}")
print(f"Ötösök:\n {otosok}")