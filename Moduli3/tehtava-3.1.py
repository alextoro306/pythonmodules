pituus = float(input("Kalastaja mikä on kuhan pituus senttimetreinä: "))

aliraja = 37

if pituus < aliraja:
    puuttuvamitta = aliraja - pituus
    print(f"Kuha on alimittainen {puuttuvamitta:.2f} cm alimmasta sallitusta rajasta")
else:
    print("Kuha on sallitun kokoinen")