intial_input = input('Enter Your Name: ')
intial_bid = int(input("Enter The Bid Amount: "))
bidders = {intial_input:intial_bid}
more_bidders = True
while more_bidders:
    choice = input("Are there more bidders")
    if choice == "yes":
        name = input("Enter Your Name: ")
        bid = int(input("Enter The Bid Amount: "))
        bidders[name] = bid
    else:
        more_bidders = False
#ChatGpt G
highest_bidder = max(bidders, key=bidders.get)
print(f"The winner is {highest_bidder} with a bid of ${bidders[highest_bidder]}")