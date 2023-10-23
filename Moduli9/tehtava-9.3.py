class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.hetkinnopeus = 0
        self.matka = 2000

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


auto = Auto("ABC123", 142)
auto.print_car()
auto.kiihdyta(60)
auto.kulje(1.5)
auto.print_car()