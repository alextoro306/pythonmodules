nimet = set()
uusinimi = set()

while True:
    nimi = input("Syötä nimi (tyhjä rivi lopettaa): ")
    
    if nimi == "":
        break
    
    if nimi in nimet:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
        uusinimi.add(nimi)
    
    nimet.add(nimi)
    
for nimi in uusinimi:
    print(nimi)