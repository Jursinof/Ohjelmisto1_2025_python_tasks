import math

kanta_str = input("Anna suorakulmion kanta: ")
korkeus_str = input("Anna suorakulmion korkeus: ")
kanta = float(kanta_str)
korkeus = float(korkeus_str)

pinta_ala = kanta * korkeus
piiri = kanta*2 + korkeus*2

print("Suorakulmion pinta-ala on: " + str(pinta_ala) + "\nSuorakulmion piiri on: " + str(piiri) + "")