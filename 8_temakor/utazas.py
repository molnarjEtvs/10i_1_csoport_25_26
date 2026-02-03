def utikoltseg_szamitas(tavolsag:int,fogyasztas:float,benzin_ar:float,utasokSzam:int = 1):
    uzemanyagFogyas = (tavolsag/100)*fogyasztas
    utTeljesKtsg = uzemanyagFogyas * benzin_ar
    egyUtasKtsg = utTeljesKtsg / utasokSzam
    return round(egyUtasKtsg)