# list
employees = ["David", "Harry", "Ron"]
print(employees[0])
print(employees[1])
print(employees[2])

# mění položku
employees[1] = "Hermiona"
print(employees)

# přidáváme obsah - jedna hodnota
employees.append("Harry")
print(employees)

# přidáváme více položek - více
employees.extend(["Crabe", "Goyle"])
print(employees)

# odstraňujeme položku - musím zadat tu konrkétné položku
employees.remove("Ron")
print(employees)