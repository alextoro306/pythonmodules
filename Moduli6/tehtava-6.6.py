import math

def main():
    kutsu = 1
    pizzaHalkaisija1 = input("Syötä ensimmäisen pyöreän pizzan halkaisija: ")
    pizzaHinta1 = input("Syötä ensimmäisen pyöreän pizzan hinta: ")
    pizzaHalkaisija2 = input("Syötä toisen pyöreän pizzan halkaisija: ")
    pizzaHinta2 = input("Syötä toisen pyöreän pizzan hinta: ")
    if pizzaHalkaisija1 != "" and pizzaHalkaisija2 != "" and pizzaHinta1 != "" and pizzaHinta2 != "":
        pizza1 = yksikkoHinta(float(pizzaHalkaisija1), float(pizzaHinta1), kutsu)
        kutsu +=1
        pizza2 = yksikkoHinta(float(pizzaHalkaisija2), float(pizzaHinta2), kutsu)

def yksikkoHinta(halkaisija, hinta, kutsuttu):
    area = (math.pi * (((halkaisija/100) / 2) ** 2))
    yksikkohinta = hinta/area
    hinta = float(round(yksikkohinta, 2))
    print(f"Pizza {kutsuttu} hinta on {hinta} euroa per neliömetri.")
main()