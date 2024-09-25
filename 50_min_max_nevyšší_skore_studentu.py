# Nejvyšší skóre v testu
# score = [98, 50, 25, 78, 92]
# print(max(score))
# print(min(score))


score = input("Zadejte skóre jednotlivých studentů oddělené čárkou a mezerou\n")        # vstup uživatele - stringy oddělené čárkou a mezerou
score_list = score.split(", ")                                                          # rozsekání na list ze stringů - s tím ještě neumí pracovat
score_list_number = []                                                                  # připravený prázdný list pro naplnění z for pomocí integerů
maximum = 0


for index in range(0, len(score_list) -1):                                              # index od 0 do délky listu
   score_list_number.append(int(score_list[index]))                                     # naplnění listu vždy na konec pomocí integerů

print(score_list_number)


for one_onumber in score_list_number:
    if one_onumber > maximum:
        maximum = one_onumber


print(f"Maximum je {maximum}")







