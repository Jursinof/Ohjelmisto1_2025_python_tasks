kuhan_pituus = float(input("Anna kuhan pituus senttimetreinä: "))

if kuhan_pituus<37:
    puutos = 37-kuhan_pituus
    print("Kuha on alamittainen, laske se takaisin järveen! Pituudesta puuttui " + str(puutos) + " cm.")
else:
    print("Hieno kala, oot sie epeli!")