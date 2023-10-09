#Enter Python code here and hit the Run button.
import random
letters =  ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',' Y','Z']
numbers = ['0','1','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','*','+']
print("Welcome to the Pypassword generator")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n "))
nr_numbers = int(input("How many numbers would you like?\n"))
password = []
for letter in range(1,nr_letters+1):
    password.append(random.choice(letters))

for number in range(1,nr_numbers+1):

    password.append(random.choice(numbers))

for symbol in range(1,nr_symbols+1):

    password.append(random.choice(symbols))

random.shuffle(password)

password_str = ""
for char in password:
    password_str += char

print(f"Your password is {password_str}")
