import os
os.system("cls")

jegyek = []

while True:
    jegy = int(input("Add meg a jegyet: "))
    if jegy == 0:
        break
    jegyek.append(jegy)

legrosszab = min(jegyek)
legjobb = max(jegyek)
db = len(jegyek)
atlag = sum(jegyek) / db

print(f"Legrosszabb:{legrosszab}\nLegjobB:{legjobb}\nÁtlag:{atlag}\ndarabszám:{db} db")
