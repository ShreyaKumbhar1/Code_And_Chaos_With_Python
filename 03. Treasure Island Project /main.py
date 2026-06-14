print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You are at a cross road. Where do you want to go?")
direction = input("Type 'left' or 'right: \n")
if direction == "left":
    print("You've come to lake. There is an inland in the middle of the lake.")
    action=input("Type 'wait' to wait for a boat. Type 'swim' to swim across:\n")
    if action == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        print("One red, one yellow and one blue.")
        door=input("Which colour do you chose?\n")
        if door=='yellow':
            print("You have won the game!")
        elif door=='red':
            print("You were burned by the fire.\nGame Over!")
        elif door=='blue':
            print("You were eaten by beasts.\nGame Over!")
        else:
            print("Game Over!")
    else:
        print("You were attacked by trout.\nGame Over!")
else:
    print("You fell into a hole.\nGame Over!")
