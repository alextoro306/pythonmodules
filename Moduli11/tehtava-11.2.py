class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.matkamittari = 0

    def aja(self, tuntimaara):
        self.matkamittari += self.huippunopeus * tuntimaara

    def tulosta_matkamittari(self):
        print(f"{self.rekisteritunnus} matkamittari: {self.matkamittari} km")

class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

    def lataa(self, latausmaara):
        self.akkukapasiteetti += latausmaara

    def aja(self, tuntimaara):
        if tuntimaara * self.huippunopeus <= self.akkukapasiteetti:
            self.akkukapasiteetti -= tuntimaara * self.huippunopeus
            super().aja(tuntimaara)
        else:
            matka_km = self.akkukapasiteetti / self.huippunopeus
            self.akkukapasiteetti = 0
            super().aja(matka_km)
            print(f"{self.rekisteritunnus} akku tyhjeni, ajaminen {matka_km} km")

    def tulosta_akkukapasiteetti(self):
        print(f"{self.rekisteritunnus} akkukapasiteetti: {self.akkukapasiteetti} kWh")

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, tankin_koko):
        super().__init__(rekisteritunnus, huippunopeus)
        self.tankin_koko = tankin_koko
        self.bensan_maara = tankin_koko

    def tankkaa(self, litroja):
        self.bensan_maara += litroja

    def aja(self, tuntimaara):
        if tuntimaara * self.huippunopeus * 0.1 <= self.bensan_maara:
            self.bensan_maara -= tuntimaara * self.huippunopeus * 0.1
            super().aja(tuntimaara)
        else:
            matka_km = self.bensan_maara / (self.huippunopeus * 0.1)
            self.bensan_maara = 0
            super().aja(matka_km)
            print(f"{self.rekisteritunnus} bensa loppui, ajaminen {matka_km} km")

    def tulosta_bensan_maara(self):
        print(f"{self.rekisteritunnus} bensan määrä: {self.bensan_maara} litraa")

sahkoauto = Sähköauto("ABC-15", 180, 52.5)
polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)

sahkoauto.aja(3)
polttomoottoriauto.aja(3)

sahkoauto.tulosta_matkamittari()
polttomoottoriauto.tulosta_matkamittari()

