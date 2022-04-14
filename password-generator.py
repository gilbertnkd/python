#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# password = "" #here we are creating a collector and passing in an emty string
# for char in range(nr_letters):#creating a loop and passing in the range the users input e.g. (4) 
#   pass_letters = random.choice(letters)#creating a variable and assiging the random items to it pulling data from list e.g. Letters
#   password += pass_letters#passing the random items from list to our password variable

# for char in range(nr_symbols):
#   pass_symbols = random.choice(symbols)
#   password += pass_symbols

# for char in range(nr_numbers):
#   pass_numbers = random.choice(numbers)
#   password += pass_numbers
# print(password)
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password = []

for char in range(nr_letters):
  password.append(random.choice(letters))


for char in range(nr_symbols):
  password.append(random.choice(symbols))

for char in range(nr_numbers):
  password.append(random.choice(numbers))
#here we are using the shuffle function to shuffle items inside of the list
random.shuffle(password)
#here we are creating a new variable we are not using the password variable anymore we create a new one
encryption = ""
# here we are assing the items in the shuffled list password to the variable encrypt
for encrypt in password:
  # we are adding values from encrypt to the variable encryption
  encryption = encryption + encrypt
#here the variables are all stored in encryption so we are finally printing them out
print(encryption)  
