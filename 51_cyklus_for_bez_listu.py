# # range
# for one_number in range(1, 5):          # 5 už tam nepatří! nevypíše ji!!!
#     print(one_number)

# # range s kroky
# for one_number in range(1, 11, 2):          # krok je 2
#     print(one_number)

# suma čísel
suma = 0
for one_number in range(1,101):
    # suma = suma + one_number
    suma += one_number

print(suma)


