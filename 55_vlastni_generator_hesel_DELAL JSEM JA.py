import random
import math

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special_char = ['%', '#', '$', '!', '&', '(', ')', '*', '+', '?']



pocet_pismen = input("Kolik písmen chcete mít ve svém heslu?\n")
pocet_cisel = input("Kolik čísel chcete mít ve svém heslu?\n")
pocet_znaku = input("Kolik speciálních znaků chcete mít ve svém heslu?\n")

pocet_pismen_list = []
pocet_cisel_list = []
pocet_znaku_list = []

for pocet in range(0, int(pocet_pismen)):
    pocet_pismen_list.append(letters[random.randint(0,len(letters))])

print(pocet_pismen_list)



