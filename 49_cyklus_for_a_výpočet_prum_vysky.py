heights = input("Vložte výšky lidí oddělené čárkou a mezerou\n")
heights_list = heights.split(", ")
suma = 0


for one_height in heights_list:             # sečte všechny hodnoty v listu
    suma = suma + int(one_height)


average = suma / len(heights_list)
print(f"Průměrná výška je: {average}.")