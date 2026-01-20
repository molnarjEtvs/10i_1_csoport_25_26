import os, random
os.system("cls")

nyeroszamok = []
while len(nyeroszamok)<5:
    sorsolt_szam = random.randint(1,90)
    if sorsolt_szam not in nyeroszamok:
        nyeroszamok.append(sorsolt_szam)
nyeroszamok.sort()

tippek = []
sorszam = 1
while len(tippek)<5:
    tipp = int(input(f"Add meg a(z) {sorszam}. tipped: "))
    if tipp>=1 and tipp<=90 and tipp not in tippek:
        tippek.append(tipp)
        sorszam+=1
tippek.sort()

print(tippek)
print(nyeroszamok)
talaltokSzama = 0
for tipp in tippek:
    if tipp in nyeroszamok:
        talaltokSzama +=1
print(f"Találatok száma: {talaltokSzama}")
