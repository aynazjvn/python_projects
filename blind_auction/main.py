
from art import logo
from os import system, name 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux
    else: 
        _ = system('clear') 
  
print(logo) 
bids = {}
bidding_is_Finished = False

def find_highest_bidder(bididing_record):
    max_bid = 0
    winner = ""
    for bidder in bididing_record:
        bid_amount = bididing_record[bidder]
        if bid_amount>max_bid:
            winner = bidder
            max_bid = bid_amount
            
    print(f"The winner is {winner} with a bid of ${max_bid}") 


while not bidding_is_Finished:
    name = input("What is your name?: \n")
    price =int(input("Whats your bid?: $\n"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")  
    if should_continue == "no":
        bidding_is_Finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":   
        clear()
       

    
  
    

    

        




 
