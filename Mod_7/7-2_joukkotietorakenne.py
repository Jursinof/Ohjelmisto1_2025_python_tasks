nimi = input("Anna nimi (tyhjä lopettaa ohjelman): ")
joukko = set()

while nimi != "":

    if nimi in joukko:
        print("Aiemmin syötetty nimi.")
    else:
        print("Uusi nimi.")

    joukko.add(nimi)
    nimi = input("Anna nimi (tyhjä lopettaa ohjelman): ")

for n in joukko:
    print(n)