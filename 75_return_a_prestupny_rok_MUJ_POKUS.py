def fce(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return 1
            else:
                return 0
        else:
            return 1
    else:
        return 0

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

year = int(input("Jaký rok chcete zkontrolovat? "))
month = int(input("Jaký měsíc chcete zkontrolovat? "))

result_prestupny = fce(year)
# print(result_prestupny)     # prestupny = 1
if result_prestupny == 1 and month == 2:
    print("Počet dní v měsíci je 29")
else:
    print(f"Počet dní v měsíci je {days_in_month[month-1]}")



    

    
