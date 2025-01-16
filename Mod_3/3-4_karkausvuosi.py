vuosiluku = int(input("Anna vuosi luku: "))

if (vuosiluku % 4 == 0 and vuosiluku % 100 != 0) or (vuosiluku % 4 == 0 and vuosiluku % 400 == 0):
    print("Ilmoittamasi vuosi on karkausvuosi.")
else:
    print("Ilmoittamasi vuosi ei ole karkausvuosi.")