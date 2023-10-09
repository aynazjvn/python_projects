import art
print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text , shift_amount , start_direction):
    end_text = ""
    if start_direction == "decode":
           shift_amount *= -1
    for char in start_text:
        if char in alphabet:
             position = alphabet.index(f"{char}")
             new_position = position+shift_amount
             new_letter = alphabet[new_position] 
             end_text += new_letter
             
        else:
            end_text += char
  
    print(f"The {start_direction}d text is {end_text}") 
should_end =False    
while not should_end:
    direction = input('Type "encode" to encrypt, type "decode" to decrypt:\n')
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 25
    caesar(start_text = text, shift_amount = shift , start_direction =direction)
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'\n")
    if restart== 'no':
        should_end =True
        print("Good bye")






