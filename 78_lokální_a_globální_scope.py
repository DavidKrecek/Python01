# Local scope a Global scope

student1 = "Harry"    # tato proměnná je globální, má glob. scope = jde všude

def test():
    student1 = "David"  # tato je lokální, je to loc. scope! neejde ven!!!
    print(student1)

test()                  # zde se použije globální scope
print(student1)         # zde je globální scope
                        # = dvě nezávsislé proměnné! = nemít stejné názvy!