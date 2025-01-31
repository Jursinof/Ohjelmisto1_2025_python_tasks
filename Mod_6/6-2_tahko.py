import random

def arpanoppa(tahko):
    noppa = random.randint(1, tahko)
    return noppa

tahkojen_maara = int(input("Anna noppasi maksimi silmäluku: "))
noppa = 0

while noppa != tahkojen_maara:
    noppa = arpanoppa(tahkojen_maara)
    print(noppa)