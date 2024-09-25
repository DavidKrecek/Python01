# Přestupný rok
# Kdy je rok přestupný?
# Rok musí být dělitelný 4
# Pokud není zároveň dělitelný 100
# tak je to přestupný rok
# Pokud je dělitelný 4, ale je dělitelný 100 a zároveň je dělitelný 400, tak je to také přestupný rok

year = int(input("Jaký rok chcete zkontrolovat? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Je to přestupný rok")
        else:
            print("Není to přestupný rok")
    else:
        print("Je to přestupný rok")
else:
    print("Není to přestupný rok")
