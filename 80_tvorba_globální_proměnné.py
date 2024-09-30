# Globální proměnná

def test():
    global my_name          # ale nemělo by se to často využívat!
    my_name = "Harry"
    print(my_name)

test()
print(my_name)              # teď už to není NameError, ale narušuji postup, jak pracovat s proměnnými, ale opatrní, jen když k tomu je závažný důvod!