# block scope   = 
number1 = 5

if number1 < 10:
    new_number = 30

print(new_number)       # má přístup i k tomu, co se udělá v if!!!





# ale když to dám do fce, tak už to dá nameError! - fce si tvoří jen local scope!!!

def create_number():
    if number1 < 10:
        new_number2 = 30

print(new_number2)      # vyhodí to NameError protože to nezná!



