import random
from logo_guessing_game import logo

print(logo)
print("Vítejte ve hře Guess secret number. Porazte počítač\nMyslím si číslo od 1 do 100.")
user_difficulty_input = input("Vyberte obtížnost. Napište 'easy' nebo 'hard': ")

random_number = random.randint(1, 100)

# na začátku počet pokusů
def attempts(user_difficulty_input):
    if user_difficulty_input == "hard":
        return 5
    else:
        return 10

user_attempts = attempts(user_difficulty_input)
print(f"Váš počet zbývajících pokusů je {user_attempts}.")
user_tip = int(input("Tipněte si číslo: "))

while user_attempts > 0:
    if user_tip == random_number:
        print("Ano, uhodli jste to!")
    elif user_tip > random_number:
        print("Příliš vysoké")
        user_attempts -= 1
    elif user_tip < random_number:
        print("Příliš nízké")
        user_attempts -= 1




