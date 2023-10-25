import random

class Auto:
    def __init__(self, nimi, nopeus):
        self.nimi = nimi
        self.nopeus = nopeus
        self.matka = 0

    def kulje(self):
        self.matka += self.nopeus

    def __str__(self):
        return f"{self.nimi}: Matka {self.matka} km, Nopeus {self.nopeus} km/h"

class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            nopeuden_muutos = random.randint(-10, 10)
            auto.nopeus += nopeuden_muutos
            auto.kulje()

    def tulosta_tilanne(self):
        print(f"{'Auto':<15}{'Matka (km)':<15}{'Nopeus (km/h)':<15}")
        for auto in self.autot:
            print(f"{auto.nimi:<15}{auto.matka:<15}{auto.nopeus:<15}")

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.matka >= self.pituus:
                return True
        return False

# Luo 10 autoa
autot = [
    Auto("Auto 1", 80),
    Auto("Auto 2", 75),
    Auto("Auto 3", 90),
    Auto("Auto 4", 85),
    Auto("Auto 5", 70),
    Auto("Auto 6", 95),
    Auto("Auto 7", 75),
    Auto("Auto 8", 78),
    Auto("Auto 9", 88),
    Auto("Auto 10", 92)
]

kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

tunti = 1
while not kilpailu.kilpailu_ohi():
    kilpailu.tunti_kuluu()
    if tunti % 10 == 0:
        print(f"Aika kulunut: {tunti} tuntia")
        kilpailu.tulosta_tilanne()
    tunti += 1

print("Kilpailu päättyi!")
kilpailu.tulosta_tilanne()