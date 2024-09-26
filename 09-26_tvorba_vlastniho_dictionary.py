

slovnik = {
    "jméno": ["David", "Magdaléna", "Matyáš", "Daniela"],
    "příjmení": ["Křečková", "Nosková", "Bobčíková", "Peřinková"],
    "místo narození": ["Mimoň", "Náchod", "Křižanov"]
}

print(slovnik["jméno"][0])

for key in slovnik:
    print(key)

for key in slovnik:
    print(slovnik[key][0])

