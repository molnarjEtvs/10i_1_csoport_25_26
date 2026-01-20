import os
os.system("cls")

szo = input("Add meg a szót: ")
hosszan = int(input("Add meg milyen hoszan: "))
kitoltoKar = input("Add meg a kitöltő karakter: ")
kozpre = szo.center(hosszan,kitoltoKar)
print(kozpre)