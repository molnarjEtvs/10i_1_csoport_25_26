emailcimek = []
with open("useradata.csv","r",encoding="utf-8") as f:
    next(f)
    for sor in f:
        adatok = sor.strip().split(";")
        emailcimek.append(adatok[1])

with open("mailcimek.txt","w",encoding="utf-8") as s:
    for email in emailcimek:
        s.write(f"{email}\n")