set1 = ["B", "A", "C"]
set2 = ["B", "A", "C"]
set3 = ["B", "A", "C"]
all_sets = [set1, set2, set3]
print(f"{set1}\n{set2}\n{set3}")
position = input("Zadejte souřadnice\n")

num1 = int(position[0])
num2 = int(position[1])

all_sets[num1][num2] = "X"


print(f"{set1}\n{set2}\n{set3}")