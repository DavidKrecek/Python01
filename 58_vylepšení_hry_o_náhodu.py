# hádací hra

import random
characters = ["Harry", "Ron", "Herminona", "Draco", "Crabbe", "Goyle", "Albus"]
character = characters[random.randint(0, len(characters)-1)]
guess = ""
# print(character)

while character != guess:
    guess = input("Uhodněte postavu z filmu Harry Potter\n")
     
print("Uhádli jste. Výborně!")
