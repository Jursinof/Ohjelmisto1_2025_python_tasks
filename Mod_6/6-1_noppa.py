import random

def arpanoppa():
    silmaluku = random.randint(1, 6)
    return silmaluku

silmaluku = 0

while silmaluku != 6:
    silmaluku = arpanoppa()
    print(silmaluku)
