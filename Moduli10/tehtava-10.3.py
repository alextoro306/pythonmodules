class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.kerros = alin_kerros
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros

    def kerros_ylös(self):
        if self.kerros < self.ylin_kerros:
            self.kerros += 1
        print(f"Hissi on kerroksessa {self.kerros}")

    def kerros_alas(self):
        if self.kerros > self.alin_kerros:
            self.kerros -= 1
        print(f"Hissi on kerroksessa {self.kerros}")

    def siirry_kerrokseen(self, kohde_kerros):
        while self.kerros < kohde_kerros:
            self.kerros_ylös()
        while self.kerros > kohde_kerros:
            self.kerros_alas()
        print(f"Hissi on nyt kerroksessa {self.kerros}")

class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lkm):
        self.hissit = [Hissi(alin_kerros, ylin_kerros) for _ in range(hissien_lkm)]

    def aja_hissiä(self, hissin_numero, kohde_kerros):
        if 0 <= hissin_numero < len(self.hissit):
            hissi = self.hissit[hissin_numero]
            hissi.siirry_kerrokseen(kohde_kerros)
        else:
            print("Hissiä ei löydy annetulla numerolla.")

    def palohälytys(self):
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(self.hissit[0].alin_kerros)
        print("Palohälytys! Kaikki hissit on ohjattu pohjakerrokseen.")

talo = Talo(1, 10, 3)
talo.aja_hissiä(0, 5)
talo.aja_hissiä(2, 7)
talo.palohälytys()
