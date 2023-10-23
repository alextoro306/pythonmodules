import random
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.hetkinnopeus = 0
        self.matka = 0

    def print_car(self):
        print(f"rekisteritunnus on: {self.rekisteritunnus}")
        print(f"huippunopeus on: {self.huippunopeus} kmh")
        print(f"hetkellinen nopeus on: {self.hetkinnopeus} kmh")
        print(f"kuljettu matka on: {self.matka} km")
        print("=======================================")

    def kiihdyta(self, nopeusmuutos):
        self.hetkinnopeus += nopeusmuutos
        if self.hetkinnopeus > self.huippunopeus:
            self.hetkinnopeus = self.huippunopeus

        elif self.hetkinnopeus < 0:
            self.hetkinnopeus = 0

    def kulje(self, tuntimaara):
        self.matka += tuntimaara * self.hetkinnopeus

autot = []

for i in range(10):
    nopeus = random.randint(100,200)
    auto = Auto(f"ABC-{i+1}", nopeus)
    autot.append(auto)

kilpailu_jatkuu = True

while kilpailu_jatkuu:
    for auto in autot:
        auto.kulje(1)
        auto.kiihdyta(random.randint(-10,15))
        auto.print_car()

        if auto.matka >= 10000:
            kilpailu_jatkuu = False

print("Auton ominaisuudet: ")
print("Rekisteritunnus /\ Huippunopeus /\ Nopeus /\ Matka")
print("--------------------------------------------------")
for auto in autot:
    print(f"{auto.rekisteritunnus} /\ -------------> {auto.huippunopeus} km/h /\ {auto.hetkinnopeus} km/h /\ {auto.matka} km")



