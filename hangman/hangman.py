import random
import hangman_art
import hangman_words
import clear

print(hangman_art.logo)
stages = [ '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
========='''
, '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
========='''
, '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
========='''
, '''
  +---+
  |   |
  O   |
  |   |
      |
      |
========='''
, '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
  +---+
  |   |
      |
      |
      |
      |
=========''']
 
chosen_word = random.choice(hangman_words.words_list)
print(f" Pssst, the solution is {chosen_word}.")
display = []
for word in chosen_word:
    display+="_"
end_of_game = False
lives = 6
while not end_of_game:
    guess =(input("Guss a letter\n")).lower()
    clear()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            if guess in display:
                print(f"You have guessed the letter {guess} already")
            else:
                display[position] = letter
                print(display)
    if guess not in chosen_word :
        print(f" You guessed {guess} that's not in the word. You lose a life!!!")
        print(stages[lives])
        lives -= 1
        if lives == 0:
            print(stages[0])
            end_of_game = True
            print("You lose!!")
    print(f"{' '.join(display)}")     
           
if "_" not in display:
        end_of_game = True
