import random

def funkce(pozice_listu):
    list[pozice_listu-1] = "X"

velikost_listu = int(input("Zadejte velikost listu - 1 až 20\n"))
pozice_listu = int(input("Zadejte pozici v listu k nahrazení znakem 'X'\n"))

list = []
for index in range(0,velikost_listu):
    nahodne_cislo = random.randint(0,100)
    list.append(nahodne_cislo)

funkce(pozice_listu)
print(list)

jen_rezetec = ""
for one_character in list:
    jen_rezetec += str(one_character)
    
print(jen_rezetec)


    
