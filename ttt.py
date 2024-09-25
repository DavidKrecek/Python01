# Nejvyšší skóre v testu
# score = [98, 50, 25, 78, 92]
# print(max(score))
# print(min(score))


score = input("Zadejte skóre jednotlivých studentů oddělené čárkou a mezerou\n")
score_list = score.split(", ")
score_list_number = []
maximum = 0


for index in range(0, len(score_list) -1):
   score_list_number.append(int(score_list[index]))

print(score_list_number)


for one_onumber in score_list_number:
    if one_onumber > maximum:
        maximum = one_onumber


print(f"Maximum je {maximum}")
print("je to v commit git")