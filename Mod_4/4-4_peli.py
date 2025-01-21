import random

arpa_luku = random.randint(1, 10)
arvaus = int(input("Arvaa kokonaisluku 1 ja 10 väliltä: "))

while arvaus != arpa_luku:
    if arvaus < arpa_luku:
        print("Liian pieni arvaus")
    elif arvaus > arpa_luku:
        print("Liian suuri arvaus")
    arvaus = int(input("Arvaa uudelleen: "))
print("Oikein")
