import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Easy Version
#password=""
#for a in range(1,nr_letters+1):
#    choose_of_letters = random.choice(letters)
#    password+=choose_of_letters
#for b in range(1,nr_symbols+1):
#    choose_of_symbols = random.choice(symbols)
#    password+=choose_of_symbols
#for c in range(1,nr_numbers+1):
#    choose_of_numbers = random.choice(numbers)
#   password+=choose_of_numbers

#print(f"Your password is: {password}")

#_____________________________________________________#

#Intense Version
password_list=[]
for a in range(1,nr_letters+1):
    choose_of_letters = random.choice(letters)      #1st Way
    password_list+=choose_of_letters
for b in range(1,nr_symbols+1):
    password_list+=random.choice(symbols)           #2nd Way
for c in range(1,nr_numbers+1):
    password_list.append(random.choice(numbers))    #3rd Way

print(password_list)
random.shuffle(password_list)
print(password_list)
password=""                                        #To convert into a String
for var in password_list:
    password+=var
print(f"Your password is: {password}")
