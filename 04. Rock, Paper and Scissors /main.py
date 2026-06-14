import random
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

game_image=[rock,paper,scissors]

print("What do you choose?")
user_choose=int(input("Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))
print("You choose: \n")
if user_choose<0 or user_choose>2:
    print("You typed an invalid choice.")
else:
    print(game_image[user_choose])

selection=random.randint(0,2)
print("Computer chose:\n")
print(game_image[selection])

#Method 1
if user_choose<0 or user_choose>2:
    print("You typed an invalid choice.")
elif user_choose==0 and selection==1:
    print("You Lose!")
elif user_choose==0 and selection==2:
    print("You Win!")
elif user_choose==1 and selection==0:
    print("You Win!")
elif user_choose==1 and selection==2:
    print("You Lose!")
elif user_choose==2 and selection==0:
    print("You Lose!")
elif user_choose==2 and selection==1:
    print("You Win!")
else:
    print("Tie!")

#Method 2
#if user_choose == selection:
#   print("Tie!")
#elif (user_choose == 0 and selection == 2) or \
#    (user_choose == 1 and selection == 0) or \
#    (user_choose == 2 and selection == 1):
#   print("You Win!")
#else:
#   print("You Lose!")
