import random

def hazeni_kostkou():
    return random.randint(1, 6)

# Simulace 10 hodů kostkou
for i in range(10):
    vysledek = hazeni_kostkou()
    print(f"Hod {i+1}: {vysledek}")
