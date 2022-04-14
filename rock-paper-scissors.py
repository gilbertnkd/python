rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

my_images = [rock, paper, scissors]
my_choice = int(input("0 for rock, 1 for paper and 2 for scissors:"))

if my_choice >=3 or my_choice < 0:
  print("you entered an invalid number, you lose")
else:
  print(my_images[my_choice])
 
  
  computer_choice = random.randint(0, 2)
  print("computer chose:")
  print(my_images[computer_choice])
  
  
  
  if my_choice == 0 and computer_choice == 2:
    print("you lose")
  elif computer_choice == 0 and my_choice ==2:
    print("you lose")
  elif computer_choice > my_choice:
    print("i lose")
  elif my_choice > computer_choice:
    print("i win")
  elif computer_choice == my_choice:
    print("draw")
