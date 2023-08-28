lista = []
    
while True:
    luku = input("Syötä luku (tyhjä rivi lopettaa): ")
        
    if luku == "":
        break
        
    number = float(luku)
    lista.append(number)
        
if lista:
    min_number = min(lista)
    max_number = max(lista)
    print("Pienin luku:", min_number)
    print("Suurin luku:", max_number)