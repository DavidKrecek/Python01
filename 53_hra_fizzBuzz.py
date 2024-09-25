# číslo dělitelné 3 = Fizz
# číslo dělitelné 5 = Buzz
# číslo dělitelné 3 a 5 = FizzBuzz
# jinak vypsat běžné číslo


for number in range(1, 101):
    if (number % 3 == 0) and (number % 5== 0):
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

        


