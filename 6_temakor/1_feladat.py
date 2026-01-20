import os
os.system("cls")

gyumolcsok = []

while True:
    gyumolcs = input("Adj meg egy gyümölcsöt: ")
    if not gyumolcs:
        break
    gyumolcs = gyumolcs.capitalize()
    gyumolcsok.append(gyumolcs)

print(gyumolcsok)