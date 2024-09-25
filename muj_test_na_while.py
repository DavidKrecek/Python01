import random
do_kolika = int(input("Napište číslo, max 100 do kolika to má náhodně generovat čísla než náhodou vygeneruje vyšší než je zadané\n"))

count = 0
list = []
variable = random.randint(0,100)
list_int = ""

while variable < do_kolika:
    list.append(variable)
    count += 1
    variable = random.randint(0,100)

for one_character in list:
    list_int += str(one_character)

print(f"celkem jsem napočítal {count}")
print(list)
print(list_int)




