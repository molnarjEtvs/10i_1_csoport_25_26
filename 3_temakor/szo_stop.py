import os
os.system("cls")

#1 megoldás:
szo = ""
while szo != "STOP":
    szo = input("Adj meg egy szót: ")
print("A program futása kész")

#2 megoldás
while True:
    szo = input("Adj meg egy szót: ")
    if szo == "STOP":
        break
    
print("A program futása kész")
