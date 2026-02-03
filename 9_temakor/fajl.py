import os
os.system("cls")

with open("szoveg.txt","r",encoding="utf-8") as f:
    for sor in f:
        print(sor.strip())

with open("iras.txt","w",encoding="utf-8") as f:
    f.write("helló világ")
