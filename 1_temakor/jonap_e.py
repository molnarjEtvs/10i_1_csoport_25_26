import os
os.system("cls")

valasz = input("Jó napod van (igen/nem)? ")
if valasz == "igen":
    print("Akkor ez egy király nap")
elif valasz == "nem":
    print("Akkor ez egy szörnyű nap")
else:
    print("Sajnos nem tudom értelmezni...")