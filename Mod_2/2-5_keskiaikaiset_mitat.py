luoti = 13.3
naula = luoti * 32
leiviska = naula * 20

leiviskat = float(input("Anna leiviskät.\n"))
print("")
naulat = float(input("Anna naulat.\n"))
print("")
luodit = float(input("Anna luodit.\n"))

leiviskat_g = leiviskat * leiviska
naula_g = naulat * naula
luodit_g = luodit * luoti

massa_g = leiviskat_g + naula_g + luodit_g
massa_kg = massa_g / 1000
kilogramma = int(massa_kg)
grammat = (massa_kg - kilogramma) * 1000

print("\nMassa nykymitojen mukaan:")
print(f"{kilogramma} kilogrammaa ja {grammat:0.2f} grammaa.")