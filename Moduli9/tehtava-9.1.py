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

auto = Auto("ABC123", 142)
auto.print_car()