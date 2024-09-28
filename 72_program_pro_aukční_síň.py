# silent auction
from auctionLogo import auction_logo
import os                 # je to os.system - pro čištění obrazovky

print(auction_logo)

bidders = {}

print("Vítejete v programu na tichou aukci")
lets_continue = "ano"

# naplnění dictionary nabízejícími
while lets_continue == "ano":
    name = input("Jaké je vaše jméno? ")
    bid = int(input("Jaká je vaše nabídku v USD? "))
    bidders[name] = bid     # ke key name to uloží value bid
    lets_continue = input("Jsou další nabízející? Napište 'ano nebo 'ne'.")
    if lets_continue == "ne":
        # vyčisti obrazovku
        os.system("cls")

# hledání nejvyšší nabídky
# highest_bid = 0

# for key in bidders:
#     winner = ""
#     if bidders[key] > highest_bid:
#         highest_bid = bidders[key]
#         winner = key

# print(f"Vítězem tiché aktuce je: {winner} s nabídkou {highest_bid} dolarů")

def highest_bid(bidders_dictionary):
    highest_bid = 0
    winner = ""
    for key in bidders_dictionary:
         if bidders_dictionary[key] > highest_bid:
             highest_bid = bidders_dictionary[key]
             winner = key

    print(f"Vítězem tiché aktuce je: {winner} s nabídkou {highest_bid} dolarů")

highest_bid(bidders)
