paalista = []

def summa(paalista):
    summa = 0
    lista = paalista
    for luku in lista:
        summa = summa + luku
    print(f"Lukujen yhteinen summa on: {summa}")
    return    
def main():
    while True:
        luku = int(input("Anna luku (luku 0 lopettaa ohjelma): "))
        if luku == 0:
            print("Lopetetaan ohjelma...")
            break
        paalista.append(int(luku))
    summa(paalista)

main()