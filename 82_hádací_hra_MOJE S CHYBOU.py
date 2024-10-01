import random
from logo_guessing_game import logo
import os


# úvodní informace
print(logo)
print("Vítejte ve hře Guess Secret Number. Porazte počítač.")
print("Myslím si číslo od 1 do 100")
difficulty = input("Vyberte obtížnost. Napiště 'easy' nebo 'hard': ")  ####

# příprava hry
secret_number = random.randint(1, 100)
print(f"Hádané číslo je {secret_number}")


def difficulty():
    difficulty = input("Vyberte obtížnost. Napište 'easy' nebo 'hard': ")
    if difficulty == "easy":
        return 10
    elif difficulty == "hard":
        return 5


# počet pokusů
def guessing_game():
    attemps = difficulty()

    another_game = ""

    while attemps > 0:
        print(f"Váš počet zbývajích pokusů je {attemps}")
        guess = int(input("Tipněte si číslo: "))

        if guess < secret_number:
            print("Příliš nízké")
            attemps -= 1
        elif guess > secret_number:
            print("Přílis vysoké")
            attemps -= 1
        else:
            print("Vyhráli jste, počítač je poražen!")
            another_game = input(
                "Napište'yes', pokud chcete pokračovat. Napište 'no', pokud chcete hru ukončit"
            )

        if attemps == 0:
            print("Prohráli jste, počítač vyhrál!")
            another_game = input(
                "Napište'yes', pokud chcete pokračovat. Napište 'no', pokud chcete hru ukončit "
            )

        if guess == "yes":
            os.system("cls")
            guessing_game()  # toto je ta rekurze = pustí to znova!
        elif another_game == "no":
            os.system("cls")
            break  # ukončuje cyklus


guessing_game()
