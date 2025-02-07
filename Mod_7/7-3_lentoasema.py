lentoasematiedot = {"EFHK":"Helsinki-Vantaa", "ESBD":"Tukholma, Arlanda", "ENCB":"Bergen", "EKCH":"Kööpenhamina"}

valinta = input("Haluatko syöttää uuden lentoaseman, hakea jo syötetyn lentoaseman tiedot vai lopettaa? (uusi/haku/lopetus): ")

while valinta != "lopetus":
    if valinta == "uusi":
        lentoasema = input("Anna lentoaseman nimi: ")
        icao = input("Anna ICAO-koodi: ")
        lentoasematiedot[icao] = lentoasema
    elif valinta == "haku":
        icao = input("Anna ICAO-koodi: ")
        print(f"{lentoasematiedot[icao]}")
    valinta = input("Haluatko syöttää uuden lentoaseman, hakea jo syötetyn lentoaseman tiedot vai lopettaa? (uusi/haku/lopetus): ")