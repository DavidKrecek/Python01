# Hangman
import random
from Hangman import stages

# uvítání a pravidla hry
print("Vítejte ve hře Hangman Harry Potter.")

# Generování náhodného slova
words = ["harry", "ronald", "albus", "hermiona"]
random_word = words[random.randint(0, 3)]

# Generování podtržítek
hidden_word = []
for one_letter in random_word:
    hidden_word.append("_")

lives = 6
print(stages[lives])

# životy
while "_" in hidden_word:                  # jede dále, dokud jsou _ ve slově
    guess = input("Zadejte hádané písmeno\n").lower()     # převede to na malé p.
    for index in range(0, len(random_word)):
        if guess == random_word[index]:
            hidden_word[index] = guess
    
    # kontrola životů
    if guess not in random_word:
        lives -= 1
        print(stages[lives])
    print(f"Počet vašich životů je {lives}")   
    if lives == 0:
        print("Prohráli jste")
        break

    # vypsání slova s podtržítky v normální podobě
    printedWord = ""
    for one_letter in hidden_word:
        printedWord += one_letter
    print(printedWord)

    # kontrola vítězství
    if "_" not in hidden_word:      # když není...!
        print("Vyhráli jste!!!")