# Dictionary = slovník
# key - value = ke slovu máte překlad

it_dictionary = {
    "String": "Text",       # stringu odpovídá text
    "Integer": "Celé číslo",            # nezáleží na pořadí ve slovníku
    "Float": "Desetinné číslo",
    "Boolean": "Pravda nepravda"    # zde čárka může a nemusí být
}

print(it_dictionary["String"])     # zde musím napst key = identifikátor!!!
print(it_dictionary["Integer"])
# print(it_dictionary["blabla"])    hodí to keyerror, protože takový key není

it_dictionary_2 = {
    0: "Text",                  # key lze nahradit indexy!
    1: "Celé číslo",         
    2: "Desetinné číslo",
    3: "Pravda nepravda"   
}

# print(it_dictionary_2[2])

# přidání hodnot do dictionary
it_dictionary_2[4] = "Uložení více hodnot"
print(it_dictionary_2)

# nastavení prázdného dictionary
empty_dictionary = {}   # a do něj lze přidávat

# vyprýzdnění dictionary
it_dictionary_2 = {}    # tímto se nastaví, že je prázdný

# měníme hodnoty v dictionary
it_dictionary_2[1] = "Textová hodnota"
print(it_dictionary_2)          # vždy se to řídí podle key, není to index!!