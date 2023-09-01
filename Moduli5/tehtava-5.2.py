lista = []

while True:
    luku = input("Syötä luku (tyhjä rivi lopettaa): ")
    lista.append(luku)    
    if luku == "":
        break
lista.sort()
print(lista)