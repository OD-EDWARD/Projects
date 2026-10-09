print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
''')
print("Welcome to treasure island")
print("Your mission is to find the treasure")
choice1 = input('You are at a cross road, where do you want to go? "left" or "right".').lower()

if choice1 == "left":
    choice2 = input('you\'ve come to a lake. There is an island in the middle of '
          'the lake. Type "wait" to wait for a boat or "swim" to swim across the lake.').lower()
    if choice2 == "wait":
        choice3 = input("You\'ve gotten to the top of the island, there are three doors red, blue and yellow. Which colour do you choose?").lower()
        if choice3 == "red":
            print("you came in through the red door so you were burned by fire. Game Over")
        elif choice3 == "blue":
            print("you came in through the blue door so you were eaten by a beast. Game Over")
        elif choice3 == "yellow":
            print("You found the treasure. You Win!")
        else:
            print("You choose a door that doesn't exist. Game Over")
    else:
        print("You got attacked by an alligator. Game Over")
else:
    print("You fell into a black hole. Game Over")


