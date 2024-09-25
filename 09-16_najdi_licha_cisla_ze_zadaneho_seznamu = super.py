user = input("Zadejte čísla oddělené čárkou a mezerou\n")               # vstup uživatele
list = user.split(", ")                                                 # rozsekání vstupu na stringy do seznamu
list_number = []
list_licha = []

for index in range(0, len(list)):                                       # načtení stringů a uložení jako integerů do novéh seznamu
    list_number.append(int(list[index]))
    
print(list_number)

for cislo in range(0, len(list_number)):                                # posouzení zda je liché a přidání do seznamu
    if list_number[cislo] % 2 == 1:
        list_licha.append(int(list_number[cislo]))

print(list_licha)



