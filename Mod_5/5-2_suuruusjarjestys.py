lista = []
luvut = input("Anna luku (tyhjä merkkijono lopettaa ohjelman): ")

while luvut != "":
    lista.append(int(luvut))
    luvut = input("Anna luku (tyhjä merkkijono lopettaa ohjelman): ")

lista.sort(reverse=True)
suurimmat_luvut = lista[:5]

print(suurimmat_luvut)