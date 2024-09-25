# je to prvočíslo? -špatně
# je to prvočíslo? = dělitelná jen 1 a samosebou bez zbytku!
# přes fci

# user_number = int(input("Zadejte číslo\n"))

# def my_function(user_number):
#         if user_number % user_number == 0:
#               print(f"Ano, toto číslo {user_number} je prvočíslo")
#         else:
#               print(f"Ne, toto číslo {user_number} není prvočíslo")

# my_function(user_number)

        
# Prvočíslo - správně
def prime_number_checker(number):
    result = "Je to prvočíslo"
    for one_number in range(2, number):
       if number % one_number == 0:
           result = "Není to prvočíslo"
    print(result)


n = int(input("Zadejte prosím číslo: "))
prime_number_checker(n)


