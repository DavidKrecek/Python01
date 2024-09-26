# Dictionary a cyklus

it_dictionary = {
    "String": "Text",      
    "Integer": "Celé číslo",          
    "Float": "Desetinné číslo",
    "Boolean": "Pravda nepravda"   
}

for key in it_dictionary:
    print(key)                    # takto vypíše keys
    print(it_dictionary[key])       # takto vypíše values

