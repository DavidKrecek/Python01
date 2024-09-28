own_dictionary = {
    "Petr": {"narození": "prosinec", "věk": 35},
    "David": {"narození": "červenec", "věk": 42}
}

print(own_dictionary["Petr"]["narození"])


own_list = [
    ["ahoj", "jak"],
    ["se mas", "mam se"],
    ["dobre","super"]
]

print(own_list[0])



# Vytvoření slovníku ve slovníku
zamestnanci = {
    'Petr': {'pozice': 'inženýr', 'věk': 35},
    'Jana': {'pozice': 'manažer', 'věk': 40},
    'Lukáš': {'pozice': 'analytik', 'věk': 28}
}

# Přístup k hodnotám
print(zamestnanci['Petr']['pozice'])  # Výstup: inženýr
print(zamestnanci['Jana']['věk'])     # Výstup: 40


for key in own_dictionary:
    # print(key)
    print(own_dictionary[key]["narození"])



