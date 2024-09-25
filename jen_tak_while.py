import random

vstup = "ano"

while vstup == "ano":
    cislo = random.randint(0,100)
    print(f"Náhodné číslo je {cislo}")
    vstup = input("Chceš pokračovat? Napiš 'ano'")

print("konec")

