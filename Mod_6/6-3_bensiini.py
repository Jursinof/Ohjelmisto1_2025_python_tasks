def muunnin(gallonat):
    litrat = gallonat * 3.785
    return litrat

gallonat = float(input("Anna bensiinin nestegallona määrä (negatiivinen luku lopettaa ohjelman): "))

while gallonat >= 0:
    litrat = muunnin(gallonat)
    print(f"Antamasi gallonat {gallonat} ovat litroina {litrat}")
    gallonat = float(input("Anna bensiinin nestegallona määrä (negatiivinen luku lopettaa ohjelman): "))
