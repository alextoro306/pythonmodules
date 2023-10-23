"""
Nyt ohjelmoidaan autokilpailu. Uuden auton kuljettu matka alustetaan automaattisesti nollaksi.
Tee pääohjelman alussa lista, joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta.
Jokaisen auton huippunopeus arvotaan 100 km/h ja 200 km/h väliltä. Rekisteritunnus luodaan seuraavasti "ABC-1", "ABC-2" jne.
Sitten kilpailu alkaa. Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:

Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan väliltä -10 ja +15 km/h väliltä.
Tämä tehdään kutsumalla kiihdytä-metodia.
Kaikkia autoja käsketään liikkumaan yhden tunnin ajan. Tämä tehdään kutsumalla kulje-metodia.
Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä.
Lopuksi tulostetaan kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna.
"""

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



