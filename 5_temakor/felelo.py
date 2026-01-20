import os, random
os.system("cls")

tanulok = []
sorszam=1
while True:
    tanulo = input(f"Add meg {sorszam}. tanuló nevét: ")
    sorszam += 1
    if not tanulo:
        break
    tanulok.append(tanulo)

felelo = random.choice(tanulok)
print(felelo)