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

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]