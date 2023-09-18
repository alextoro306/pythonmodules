import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='halorvalor',
         autocommit=True
         )

def haemaakoodi(lentokentta):
    sql = ("SELECT type, COUNT(type) as amount FROM airport WHERE iso_country = %s GROUP BY type")
    kursori = yhteys.cursor()
    kursori.execute(sql, (lentokentta,))
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        return tulos
def kysely():
    maakoodiSyote = input("Syötä maakoodi: \n")
    while maakoodiSyote!="":
        haettava = haemaakoodi(maakoodiSyote)
        print(f"{haettava[1] ,haettava[4]}")
        maakoodiSyote = input("Syötä maakoodi: \n")
kysely()
