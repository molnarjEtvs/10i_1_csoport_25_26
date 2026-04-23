import random
nyeroSzamok = []
'''
for x in range(5):
    szam = random.randint(1,90)
    if szam not in nyeroSzamok:
        nyeroSzamok.append(szam)
print(nyeroSzamok)
'''

while len(nyeroSzamok)<5:
    szam = random.randint(1,90)
    if szam not in nyeroSzamok:
        nyeroSzamok.append(szam)

print(nyeroSzamok)

while True:
    szam = random.randint(1,90)
    if szam not in nyeroSzamok:
        nyeroSzamok.append(szam)
    if len(nyeroSzamok) == 5:
        break
print(nyeroSzamok)