def vuodenaika(kuukausi):
    vuodenajat = ("kevät", "kesä", "syksy", "talvi")

    if 0 < kuukausi < 3 or kuukausi == 12:
        return vuodenajat[3]
    elif 2 < kuukausi < 6:
        return vuodenajat[0]
    elif 5 < kuukausi < 9:
        return vuodenajat[1]
    elif 8 < kuukausi < 12:
        return vuodenajat[2]
    else:
        return "virheellinen numero"

kuukausi = int(input("Anna kuukauden numero: "))
vuodenaika = vuodenaika(kuukausi)

print(vuodenaika)