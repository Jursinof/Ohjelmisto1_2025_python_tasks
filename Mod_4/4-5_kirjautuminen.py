tunnus = "python"
salasana = "rules"
tunnus_kayt = input("Anna käyttäjä tunnus: ")
salasana_kayt = input("Anna salasana: ")
maara = 1

while (tunnus_kayt != tunnus and salasana_kayt != salasana) and maara != 5:
    maara = maara + 1
    tunnus_kayt = input("Anna käyttäjä tunnus: ")
    salasana_kayt = input("Anna salasana: ")
if tunnus_kayt == tunnus and salasana_kayt == salasana:
    print("Tervetuloa")
elif maara == 5:
    print("Pääsy evätty")