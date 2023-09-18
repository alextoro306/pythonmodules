import mysql.connector
from geopy.distance import geodesic

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='halorvalor',
         autocommit=True
         )

def haeKoordinaatit(icaokoodi):
    sql = "SELECT latitude_deg, longitude_deg FROM airport "
    sql += " WHERE ident = %s"
    kursori = yhteys.cursor()
    kursori.execute(sql, (icaokoodi,))
    tulos = kursori.fetchone()
    if tulos:
        return tulos
    else:
        return None

lentokentta1 = input("Anna ekan lentokentän ICAO-koodi: ")
lentokentta2 = input("Anna tokan lentokentän ICAO-koodi: ")

koordinaatit1 = haeKoordinaatit(lentokentta1)
koordinaatit2 = haeKoordinaatit(lentokentta2)

if koordinaatit1 and koordinaatit2:
    koordinaatit1 = (koordinaatit1[0], koordinaatit1[1])
    koordinaatit2 = (koordinaatit2[0], koordinaatit2[1])

    etaisyys = geodesic(koordinaatit1, koordinaatit2).kilometers

    print(f"Etäisyys lentokenttien {lentokentta1} ja {lentokentta2} välillä on {etaisyys} kilometriä.")