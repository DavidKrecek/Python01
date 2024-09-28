# funkce a return

# def sum(number1, number2):
#     print(number1 + number2)
# sum(5, 10)

# def better_name(first_name, second_name):
#     first_name = first_name.capitalize()
#     second_name = second_name.capitalize()
#     return f"{first_name} {second_name}"             # vrátí to ten řetězec

def better_name(first_name, second_name):
    full_name = first_name + " " + second_name
    return full_name.title()                           # druhý způsob

result = better_name("david", "křeček")
print(result)