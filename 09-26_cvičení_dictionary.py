dictionary = {
    "první": "David",
    "druhý": "Magdaléna",
    "třetí": "Daniela",
    "čtvrtý": "Matyáš"
}


# vytiskne vše - keys a values
print(dictionary)

# # vytiskne jen keys
for key in dictionary:
    print(key)

# # vytiskne jen values
for key in dictionary:
    print(dictionary[key])


# od Magduly:
for hodnota in dictionary.keys():
    print(hodnota)

for hodnota in dictionary.values():
    print(hodnota)

for hodnota in dictionary.items():
    print(hodnota)

