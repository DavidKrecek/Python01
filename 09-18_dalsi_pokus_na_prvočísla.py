print("Ověříme si zde, že zadané číslo je prvočíslo, tj. je dělitelné jen sebou a 1")
user_input = int(input("Zadejte prvočíslo:\n"))

def fce(user_input):
    result = "Je to prvočíslo"
    for k in range(2, user_input):
        if user_input % k == 0:
            result = "Není to prvočíslo"
    print(result)

fce(user_input)







