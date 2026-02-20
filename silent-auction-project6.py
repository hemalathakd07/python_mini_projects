import os
def bid_winner(bidder_details):
    highest_bid_price=0
    winner=""
    for i in bidder_details:
        bid_price=bidder_details[i]
        if bid_price>highest_bid_price:
            highest_bid_price=bid_price
            winner=i
    
    print(f"The bid winner is {winner} with the highest bid price of {highest_bid_price}")

flag=False
bidder_details={}
while not flag:
    name=input("Enter the name of the bidder:")
    price=int(input("Enter the bid price:"))
    bidder_details[name]=price
    next_bidder=input("Is there any other bidder:(enter yes/no)")
    if next_bidder=="no":
        flag=True
        bid_winner(bidder_details)
    elif next_bidder=="yes":
        os.system("cls")