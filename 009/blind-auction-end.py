from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo
clear()
print(logo)
print("Welcome to the secret auction program.")
bids = {}
bidding_finished = False


def find_highest_bid(bid_list):
    winner_bid = 0
    winner_name = ""
    for bidder in bid_list:
        if bid_list[bidder] > winner_bid:
            winner_name = bidder
            winner_bid = bid_list[bidder]

    print(f"The winner is {winner_name} with a bid of {winner_bid}")


while not bidding_finished:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bids[name] = bid

    response = input("Are there any other bidders? Type 'yes' or 'no'.")
    if response == "no":
        bidding_finished = True
        find_highest_bid(bids)
    elif response == "yes":
        bidding_finished = False
        clear()

