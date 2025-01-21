import random

pistemaara_N = int(input("Anna arvottavien pisteiden määrä: "))
maara = 0
ympyra_maara_n = 0

while maara < pistemaara_N:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 < 1:
        ympyra_maara_n = ympyra_maara_n + 1
    maara = maara + 1

pii_likiarvo = 4 * ympyra_maara_n / pistemaara_N

print(f"Piin likiarvo on " + str(pii_likiarvo) + "")
