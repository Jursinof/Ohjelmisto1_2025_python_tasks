def laskuri(lista):
    summa = 0
    for n in lista:
        summa += n
    return summa

lista = []
kokonaisluvut = input("Anna kokonaisluku (tyhjä merkkijono lopettaa ohjelman): ")

while kokonaisluvut != "":
    lista.append(int(kokonaisluvut))
    kokonaisluvut = input("Anna kokonaisluku (tyhjä merkkijono lopettaa ohjelman): ")

summa = laskuri(lista)
print(f"{summa}")
