tuuma = float(input("Anna tuuma määrä, jonka haluat senttimetreinä: "))
sentti = 2.54
tulo = 0

while tuuma >= 0:
    tulo = tuuma * sentti
    print(str(tulo))
    tuuma = float(input("Anna tuuma määrä, jonka haluat senttimetreinä: "))