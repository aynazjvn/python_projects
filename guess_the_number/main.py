import random
import os
from art import logo

def check_guess(guess,number):
    if guess>number:
        message = "It's too high"
        return message
    elif guess<number:
        message = "It's too low"
        return message
    else:
        message = "You win . you've guessed the correct number"
        return message
       
        
def play_game():
    print(logo)
    game_is_finished = False    
    print("Welcome to the Number Guessing Game !")
    print("I'm thinking of a number between 1 and 100 .")
    rand_number = random.randint(1,100)
    print(rand_number)
    level = input("Choose a dificulty. Type 'easy' or 'hard':")
    if level == "easy":
        attempts = 10
    else:
        attempts = 5        
    print(f"You have {attempts} attempts remaining to guess the number")
    guess = int(input("guess your number:"))
    while not game_is_finished:
        if attempts>1:
            message =check_guess(guess,rand_number)
            print(message)
            if message == "It's too low" or message == "It's too high":
                attempts-=1
                print(f" You have {attempts} attempts remaining to guess the number")
                guess = int(input("guess again:"))
        else:
            print("You lose")
            os.system('cls')
            game_is_finished = True
            play_game()
                    
       
play_game()            
            
        
            
    
    


