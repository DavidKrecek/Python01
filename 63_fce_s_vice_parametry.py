# fce s více parametry
def greet(name, location):
    print(f"Ahoj, já jsem {name} a pocházím z města {location}")

# greet("David", "České Budějovice")       

# positional arguments                      # záleží na pořadí!!!
greet("České Budějovice", "David")

# keyword arguments
greet(name="Martina", location="Tábor")     # nezáleží na pořadí!!!



