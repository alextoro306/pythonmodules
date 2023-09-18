import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='halorvalor',
         autocommit=True
         )

def haeMaakoodi(icaokoodi):
    sql = "SELECT name, iso_region FROM airport "
    sql += " WHERE ident = '" + icaokoodi + "' "
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount >0:
        for i in tulos:
            print(i)
    return


icaokoodi = input("Anna ICAO-koodi: ")
haeMaakoodi(icaokoodi)