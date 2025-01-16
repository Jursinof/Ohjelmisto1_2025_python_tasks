sukupuoli = input("Anna biologinen sukupuolesi (nainen/mies): ")

if sukupuoli=="nainen":
    hemoglobiini = float(input("Anna hemoglobiiniarvosi (g/l): "))
    if hemoglobiini<117:
        print("Hemoglobiiniarvosi on alhainen.")
    elif 117<=hemoglobiini<=175:
        print("Hemoglobiiniarvosi on normaali.")
    else:
        print("Hemoglobiiniarvosi on korkea.")
elif sukupuoli=="mies":
    hemoglobiini = float(input("Anna hemoglobiiniarvosi (g/l): "))
    if hemoglobiini<134:
        print("Hemoglobiiniarvosi on alhainen.")
    elif 134<=hemoglobiini<=195:
        print("Hemoglobiiniarvosi on normaali.")
    else:
        print("Hemoglobiiniarvosi on korkea.")
else:
    print("Kirjoititko sukupuolen oikein?")