vstup = input("Zadejte hodnoty oddělené čárkou:\n")             # input str
list = vstup.split(", ")                                        # rozsekání na str do listu
list_integer = []                                               # prázdný list k naplnění od for

for index in list:                                              # 
    # list.append(int(list[index]))
    print(index)

print(list_integer)





# for index in range(0, len(score_list) -1):                                              # index od 0 do délky listu
#    score_list_number.append(int(score_list[index]))                                     # naplnění listu vždy na konec pomocí integerů

# print(score_list_number)