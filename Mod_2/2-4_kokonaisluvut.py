import math

eka_luku = input("Anna ensimmäinen kokonaisluku: ")
toka_luku = input("Anna toinen kokonaisluku: ")
kolmas_luku = input("Anna kolmas kokonaisluku: ")

summa = int(eka_luku) + int(toka_luku) + int(kolmas_luku)
tulo = int(eka_luku) * int(toka_luku) * int(kolmas_luku)
keskiarvo = (int(eka_luku) + int(toka_luku) + int(kolmas_luku)) / 3

print("Lukujen summa on " + str(summa) + "\nLukujen tulo on " + str(tulo) + "\nLukujen keskiarvo on " + str(keskiarvo) +"")