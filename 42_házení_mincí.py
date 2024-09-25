import random
import math
# side = math.ceil(random.random() * 2) # prvni varianta, jako přes procenta a to zaokrouhlit nahoru

side = random.randint(0,1)              # druhá varianta
# je to náhodné celé číslo z rozsahu!

if side == 1:
    print("hodil jsi panna")
else: 
    print("hodil jsi orel")




# print(math.ceil(random.random() * 6))   # házení kostkou



