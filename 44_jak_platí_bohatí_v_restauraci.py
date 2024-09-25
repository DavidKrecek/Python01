import random

names = input("Napiš mi jména všech, ale oddělené čárkou\n")
print(names)

list_people = names.split(", ")         # udělám z toho list - oddělím pomocí ", "
random_number = random.randint(0,len(list_people)-1)

print(f"{list_people[random_number]} bude dnes platit účet")


