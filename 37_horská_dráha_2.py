print("Vítejte na horské dráze")
height = int(input("Jaké je vaše výška v cm?\n"))
bill = 0

if height >= 87:
    print("Můžete jet na horské dráze.")
    age = int(input("Jaký je váš věk?\n"))
    if age < 12:
        bill = 50
        print("Cena vašeho lístk je 50 Kč")
    elif age >= 12 and age <= 18:
        bill = 100
        print("Cena vašho lístku je 100 Kč")
    elif age >= 40 and age <= 50:
        bill = 0 
    else:
        bill = 150
        print("Cena vašeho lístku je 150 Kč")

    photo = input("Chcete během jízdy vyfotit? ano nebo ne?\n")
    if photo == "ano":
        bill += 40

    print(f"Vaše cena je {bill} Kč")
else:
    print("Omlouváme se, ale na horské ráze jet nemůžete.")
