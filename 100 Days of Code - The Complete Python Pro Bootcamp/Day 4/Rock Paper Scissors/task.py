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

computer_choice = random.choice([rock, paper, scissors])
print("Welcome to the rock, paper, scissors game! ")
human_choice_num = int(input("\nEnter 0 for Rock, 1 for Paper and 2 for Scissors: "))

if human_choice_num > 2 or human_choice_num < 0:
    print("Please enter a valid choice.")
else:
    if human_choice_num == 0:
        human_choice = rock
    elif human_choice_num == 1:
        human_choice = paper
    else:
        human_choice = scissors


    print("You Chose: " + "\n" + human_choice)
    print('''
#######################################################################################################################
    ''')
    print("Computer Chose: " + "\n" + computer_choice)

    if computer_choice == human_choice:
        print("Oops! it's a tie!")
    else:
        if computer_choice == rock:
            if human_choice == paper:
                print("You Won!")
            else:
                print("You Lost!")
        if computer_choice == paper:
            if human_choice == rock:
                print("You Lost!")
            else:
                print("You Won!")
        if computer_choice == scissors:
            if human_choice == rock:
                print("You Won!")
            else:
                print("You Lost!")