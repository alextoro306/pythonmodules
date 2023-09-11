lista = []

while True:
    nimi = input("Syötä nimi (tyhjä rivi lopettaa): ")  
    
    if nimi == nimi:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
    
    if nimi == "":
        break
