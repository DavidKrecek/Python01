# for n in range(1, 100):
#     n = int(n)
#     prime_number_checker(n)
#     prime_list = ""

#     def prime_number_checker(number):
#         for one_number in range(2, number):
#         if number % one_number == 0:
#             prime_list.append()




def eratosthenovo_sito(max_cislo):
    sito = [True] * (max_cislo + 1)
    sito[0] = sito[1] = False  # 0 a 1 nejsou prvočísla
    for i in range(2, int(max_cislo**0.5) + 1):
        if sito[i]:
            for j in range(i * i, max_cislo + 1, i):
                sito[j] = False
    return [i for i, prvocislo in enumerate(sito) if prvocislo]

# Testování
prvocisla = eratosthenovo_sito(1_000_000)
print(prvocisla)
        


