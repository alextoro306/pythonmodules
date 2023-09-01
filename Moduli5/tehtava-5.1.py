import random

arpakuutio = int(input("Anna arpakuutioiden lukumäärä: "))

for arpakuutio in range(arpakuutio):
    arpakuutioarvo = random.randint(1, 6)
    vastaus = arpakuutioarvo + arpakuutioarvo
    print(f"arpakuutioiden arvo on: {vastaus}")
