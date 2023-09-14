lentoasema = {}

while True:
    print("\nValitse toiminto:")
    print("1. Syötä uusi lentoasema")
    print("2. Hae lentoaseman tiedot")
    print("3. Lopeta")
    
    valinta = input("Valitse 1 tai 2 tai 3: ")
    
    if valinta == "1":
        icao_koodi = input("Syötä lentoaseman ICAO-koodi: ")
        nimi = input("Syötä lentoaseman nimi: ")
        lentoasema[icao_koodi] = nimi
        print("Lentoasema tallennettu.")
    elif valinta == "2":
        icao_koodi = input("Syötä etsittävän lentoaseman ICAO-koodi: ")
        nimi = lentoasema.get(icao_koodi)
        if nimi:
            print(f"Lentoaseman nimi: {nimi}")
        else:
            print("Lentoasemaa ei löytynyt.")
    elif valinta == "3":
        break

print("Ohjelma päättyy...")