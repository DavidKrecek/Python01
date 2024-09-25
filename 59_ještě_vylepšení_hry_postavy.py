# hádací hra

print("Vítejte v hádací hře Harry Potter")
import random
characters = ["Harry", "Ron", "Hermiona", "Draco", "Crabbe", "Goyle", "Albus"]
character = characters[random.randint(0, len(characters)-1)]
guess = ""      # prázdný string
guess_count = 3

while character != guess:
    if guess_count != 0:
        guess = input("Uhodněte postavu z filmu Harry Potter\n")
        guess_count -= 1
    else:
       print(f"Počet pokusů k hádání je vyčerpán. Hledalo se slovo {character}.")
       break                                            # = přerušení while!
        
    if character == guess:
       print(f"Uhádli jste. Výborně! Hádané slovo bylo {character}.")
