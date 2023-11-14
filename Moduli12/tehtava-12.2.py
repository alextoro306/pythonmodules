import requests

def main():
    paikkakunta = input("Syötä paikkakunnan nimi: ")
    while paikkakunta !="":

        api_avain = 'https://openweathermap.org/api'

        url = f"http://api.openweathermap.org/data/2.5/weather?q={paikkakunta}&appid={api_avain}"
        vastaus = requests.get(url)
        saa_tiedot = vastaus.json()

        if saa_tiedot["cod"] == "404":
         print("Paikkakuntaa ei löytynyt.")
        else:
            saa_tila = saa_tiedot["weather"][0]["description"]
            lampotila_kelvin = saa_tiedot["main"]["temp"]

            lampotila_celsius = round(lampotila_kelvin - 273.15, 1)

            print("===============================================")
            print(f"= Sää paikkakunnalla {paikkakunta}: {saa_tila}")
            print(f"= Lämpötila: {lampotila_celsius} °C")
            print("===============================================")
        paikkakunta = input("Syötä paikkakunnan nimi: ")
main()