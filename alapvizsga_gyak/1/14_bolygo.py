import os
os.system('cls')

def bolygoRogzites():
    bolygok = []
    while True:
        bolygo = input("add meg a bolygot")
        if not bolygo:
            break  
        bolygo = bolygo.capitalize()
        bolygok.append(bolygo)
    return bolygok

def bolygoElemzes(bolygok:list):
    db = len(bolygok)
    print(f"{db} bolygó került rögzítésre")
    dd = 0
    for bolygo in bolygok:
        if len(bolygo) == 4:
            dd+=1
    fuzes = "_$_".join(bolygok)
    print(f"Rögzitett bolygok: {fuzes}")
    print(f"4 betusek szama: {dd}db")

a = bolygoRogzites()
bolygoElemzes(a)