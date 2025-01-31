import math
def yksikko_laskin(halkaisija, hinta):
    sade_m = (halkaisija / 2) / 100
    pinta_ala = math.pi * (sade_m ** 2)
    hinta_neliometri = hinta / pinta_ala
    return hinta_neliometri

halkaisija1 = float(input("Anna ensimmäisen pizzan halkaisija (senttimetreinä): "))
hinta1 = float(input("Anna ensimmäisen pizzan hinta (euro): "))

halkaisija2 = float(input("Anna toisen pizzan halkaisija (senttimetreinä): "))
hinta2 = float(input("Anna toisen pizzan hinta (euro): "))

yksikkohinta1 = yksikko_laskin(halkaisija1, hinta1)
yksikkohinta2 = yksikko_laskin(halkaisija2, hinta2)

print(f"Ensimmäisen pizzan yksikköhinta on: {yksikkohinta1:.2f} €/m2")
print(f"Toisen pizzan yksikköhinta on: {yksikkohinta2:.2f} €/m2")

if yksikkohinta1 < yksikkohinta2:
    print("Ensimmäinen pizza on parempi diili!")
elif yksikkohinta1 > yksikkohinta2:
    print("Toinen pizza on parempi diili!")
else:
    print("Molemmat pizzat ovat yhtä hyvä diili.")