class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

    def __str__(self):
        return f" Julkaisu: " + self.nimi
    
    def tulosta_tiedot(self):
        print(self)


class Kirja(Julkaisu):
    def __init__(self, nimi, kirjailija, sivumäärä):
        self.kirjailija = "Rosa Liksom"
        self.sivumäärä = 200
        super().__init__(nimi)

    def __str__(self):
        return super().__str__() + f" Kirjoittaja: {self.kirjailija} Sivumäärä: {self.sivumäärä}"

class Lehti(Julkaisu):
    def __init__(self, nimi, päätoimittaja):
        self.päätoimittaja = "Aki Hyyppä"
        super().__init__(nimi)

    def __str__(self):
        return super().__str__() + f" Kirjoittaja: {self.päätoimittaja}"
        
def main():
    kirja = Kirja("Hytti n:o 6", "Rosa Liksom", 200)
    lehti = Lehti("Aku Ankka", "Aki Hyyppä")
    print(kirja)
    print(lehti)
main()