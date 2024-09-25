import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special_char = ['%', '#', '$', '!', '&', '(', ')', '*', '+', '?']

print("Generátor hesel")
num_letters = int(input("Kolik písmen chcete mít ve svém heslu?\n"))
num_numbers = int(input("Kolik čísel chcete mít ve svém heslu?\n"))
num_special_char = int(input("Kolik speciálních znaků chcete mít ve svém heslu?\n"))

# písmena, čísla a speciální znaky, se kterými budeme pracovat
result = []

for index in range(0, num_letters):      # tu koncovou hodnotu to už nebere
    random_number = random.randint(0, len(letters)-1)   # pozor, čísluje se od nuly!!!
    result.append(letters[random_number])

for index in range(0, num_numbers):
    random_number = random.randint(0, len(numbers) -1)
    result.append(numbers[random_number])

for index in range(0, num_special_char):
    random_number = random.randint(0, len(special_char) -1)
    result.append(special_char[random_number])

print(result)

# přeskupení - zpřeházení
# trasnslator = ""

# for index in range(0, 10):      # 11 to už nebere, takže to bude 0 až 9!, je to "do!"
#     random_index1 = random.randint(0, len(result)-1)
#     random_index2 = random.randint(0, len(result)-1)

#     translator = result[random_index2]
#     result[random_index2] = result[random_index1]
#     result[random_index1] = translator´


random.shuffle(result)          # spec fce pro random prohození řetězců!
print(result)

# převod listu na string
result_password = ""

for one_character in result:    # převede list na string
    # result_password = result_password + one_character
    result_password += one_character

print(result_password)