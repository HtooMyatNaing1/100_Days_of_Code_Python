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
print("Your mission is to find the treasure.\n")

print("You are at the cross road. Where do you want to go?")
left_or_right = input("Left or Right (Enter 'Left' or 'Right'? ").lower()

if left_or_right == "left":
    print("You've got to a big lake and there is an island in the middle of the lake.")
    swim_or_boat = input("Type 'Swim' to swim across or 'Wait' to wait for the boat: ").lower()
    if swim_or_boat == "swim":
        print("OMG! You really did swim across the lake. You really deserve it!")
        door_chosen = input("However, you must choose one of three doors to get to the treasure box. ('Red' OR 'Blue' OR 'Yellow') ").lower()
        if door_chosen == "yellow":
            print("Congratulations! You really are the one for this treasure.")
        else:
            print("Oops! You chose the wrong door. Game Over!")
    else:
        print("Oops! The boatman knows about the treasure and he killed you to rob the treasure. Game Over!")
else:
    print("Oops! There's a manhole on the right. Game Over!")


