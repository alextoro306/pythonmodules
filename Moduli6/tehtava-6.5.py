lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def parillinen(lista):
    uusi = []
    for luku in lista:
        if luku % 2 == 0:
            uusi.append(luku)
    return uusi

print(lista)
print(parillinen(lista))