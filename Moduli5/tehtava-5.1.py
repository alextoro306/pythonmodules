import random

arpakuutio = int(input("Anna arpakuutioiden lukumäärä: "))

summa = 0

for arpakuutio in range(arpakuutio):
    arpakuutioarvo = random.randint(1, 6)
    summa += arpakuutioarvo
    print(f"arpakuutioiden arvo on: {arpakuutioarvo}")

print(f"arpakuutioiden summa on: {summa}")
