import random

vastaus = random.randint(1, 10)

while True:
    arvaus = int(input("Arvaa luku: "))

    if arvaus == vastaus:
        print("Oikein")
    
    elif arvaus < 1:
        print("Liian pieni arvaus")

    elif arvaus > 10:
        print("Liian suuri arvaus")