import os
os.system("cls")

termekek = []
sorszam = 1
while True:
    termek = input(f"Add meg a(z){sorszam}. termék nevét: ")
    os.system("cls")
    sorszam += 1
    if termek == "":
        break
    termekek.append(termek)

torlendo = input("Add meg a törlendő terméket: ")
if torlendo in termekek:
    termekek.remove(torlendo)
    print(f"A(z) {torlendo} törölve lett")
else:
    print("Nincs ilyen termék a listában")