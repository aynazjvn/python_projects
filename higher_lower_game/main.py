from game_data import data
import random
from art import logo , vs
import os


game_shoud_continue= True

def format_data(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country= account["country"]
    return f" {account_name}, a {account_descr} from {account_country}"

def check_answer(guess,a_follower_count,b_follower_count):
    if a_follower_count>b_follower_count:
         return guess == "a"        
    else:
        return guess == "b"
    
account_b = random.choice(data)        
print(logo)
score=0
while game_shoud_continue:
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A:{format_data(account_a)}")
    print(vs)
    print(f"Against B:{format_data(account_b)}")
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    guess = input("Which one? Type 'A ' or 'B'").lower()


    is_correct = check_answer(guess,a_follower_count,b_follower_count)    
    os.system('cls')
    print(logo)
    

    if is_correct:
        score+=1
        print(f"Your right your current score is {score}")
    else:
        game_shoud_continue = False
        print (f" Sorry that's wrong. your final score is {score}")
        
        
            
    
   
    
   
    
    