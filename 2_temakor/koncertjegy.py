import os
os.system("cls")

szektorAr = 6500
paholyAr = 9800
vegosszeg = 0
kedvezmenySzorzo = 0.75

hely = input("Add meg hov szeretnél jegyet? Páholy(P), Szektor(S): ")
db = int(input("Add meg a jegyek számát: "))
diake = input("Diák vagy? igen(i), nem(n): ")

if hely == "P":
    vegosszeg = paholyAr * db
elif hely == "S":
    vegosszeg = szektorAr * db
else:
    print("NINCS ILYEN JEGYTÍPUS")

if diake == "i":
    vegosszeg = vegosszeg * kedvezmenySzorzo

print(f"A fizetendő összeg: {vegosszeg} Ft")