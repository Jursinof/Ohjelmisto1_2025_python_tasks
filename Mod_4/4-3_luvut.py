kayttaja_syote = input("Anna luku (tyhjä merkkijono lopettaa ohjelman): ")
pieni_luku = iso_luku = kayttaja_syote

while kayttaja_syote != "":
    if kayttaja_syote < pieni_luku:
        pieni_luku = kayttaja_syote
    elif kayttaja_syote > iso_luku:
        iso_luku = kayttaja_syote
    kayttaja_syote = input("Anna luku (tyhjä merkkijono lopettaa ohjelman): ")

print("Pienin luku oli: " + str(pieni_luku) + "\nIsoin luku oli: " + str(iso_luku))
