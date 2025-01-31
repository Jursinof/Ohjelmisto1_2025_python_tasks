def pariton_muunnin(lista):
    lista_parilliset = []
    for n in lista:
        if n % 2 == 0:
            lista_parilliset.append(n)
    return lista_parilliset

lista_koko = []
kayttaja_syote = input("Anna kokonaisluku (tyhjä syöte lopettaa ohjelman): ")

while kayttaja_syote != "":
    lista_koko.append(int(kayttaja_syote))
    kayttaja_syote = input("Anna kokonaisluku (tyhjä syöte lopettaa ohjelman): ")

parilliset = pariton_muunnin(lista_koko)

print(f"Alkuperäinen lista: {lista_koko}")
print(f"Parilliset luvut: {parilliset}")