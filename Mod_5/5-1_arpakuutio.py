import random

arpa_kuutiot = []
arpa_maara = int(input("Anna arpakuutioiden määrä: "))
i = 1
summa = 0

while i <= arpa_maara:
    noppa = random.randint(1, 6)
    arpa_kuutiot.append(noppa)
    i += 1

for arpa in arpa_kuutiot:
    summa += arpa
    print(f"{arpa}")

print(f"Arpakuutioiden summa on: {summa}")
