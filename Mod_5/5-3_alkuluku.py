luku = int(input("Anna kokonaisluku: "))
jakavat_luvut = []

if luku < 2:
    print("Luku ei ole alkuluku.")
else:
    i = 2

    while i < luku:
        if luku % i == 0:
            jakavat_luvut.append(i)
        i += 1

    if len(jakavat_luvut) == 0:
        print(f"{luku} on alkuluku.")
    else:
        print(f"{luku} ei ole alkuluku.")