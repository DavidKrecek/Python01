# vypočítejte BMI, který se počítá jako
# BMI = váha v kg / (výška v m) na m2

height = input("Zadejte svou výku v metrech:\n")
weight = input("Zadejte svou váhu v kg:\n")

bmi = int(weight) / (float(height) * float(height))
bmi = int(bmi)
print("Váš BMI je: " + str(bmi))

