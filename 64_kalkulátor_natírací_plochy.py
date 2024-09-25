import math

def fce_natirani_plochy(vyska, sirka):
    pocet = math.ceil((vyska * sirka) / 5)
    print(f"Budete potřebovat {pocet} plechové barvy")

vyska = float(input("Výška zdi: "))
sirka = float(input("Šířka zdi: "))

fce_natirani_plochy(vyska, sirka)
