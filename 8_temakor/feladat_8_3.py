import os,random
os.system("cls")

def jelszo_genaralas(hossz:int):
    karakterek = "0123456789qwertzuiopasdfghjklyxcvbnm"
    karakterekLista = list(karakterek)
    jelszo = ""
    for _ in range(hossz):
        jelszo += random.choice(karakterekLista)
    return jelszo

def biztonsagi_elemzes(jelszo:str):
    if len(jelszo)<5:
        print("Gyenge jelszó! (Túl rövid)")
    elif len(jelszo)>=5 and len(jelszo)<=8:
        print("Közepes jelszó.")
    else:
        print("Erős jelszó")

j = jelszo_genaralas(5)
biztonsagi_elemzes(j)