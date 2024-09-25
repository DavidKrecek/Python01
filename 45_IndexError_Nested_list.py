# IndexError = když je index mimo rozsah
gryffindor = ["David", "Harry", "Ron", "Hermiona"]
slytherin = ["Draco", "Crabbe", "Goyle"]

number = len(gryffindor)
print(gryffindor[number - 1])

# nested list - spojení listů dohromady
students = [gryffindor, slytherin]
print(students[0][1])   # vypíše pozici 1 ve 2 listech a vtom ještě pozici 1 (tedy toho druhého)

