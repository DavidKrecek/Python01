def greet():
    print("Ahoj")
    print("Já jsem David")
    print("Na shledanou")

def greet_name(name):                           # v závorce je parametr name
    print(f"Ahoj, já jsem {name}")

greet_name("David")                 # posílám tam argument = konkrét hodnota
greet_name("Harry")
greet_name("Hermiona")

#argument se stane obsahem proměnné parametru!!!