leiviskat = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

naulat = naulat + leiviskat * 20
luodit = luodit + naulat * 32
paino = luodit * 13.3
kilo = 0

while paino > 1000:
    kilo = kilo + 1
    paino = paino - 1000
print("Massa nykymittojen mukaan: ")
print(f"{kilo} kilogrammaa ja {paino:.2f} grammaa.")