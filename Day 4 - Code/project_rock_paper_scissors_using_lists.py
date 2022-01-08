'''
RULES OF THE GAME
1.Rock beats Scissors
2.Scissors beats Paper
3.Paper beats Rock
'''
# LOGIC
# 0 represents rock
# 1 represents paper
# 2 represents scissors


import random

rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")


paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")


scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

images = [rock, paper, scissors]
while(True):
    computer_choice = random.randint(0, 2)
    user_choice = int(input("Choose rock(0), paper(1) or scissors(2): "))

    print(f"You choose {images[user_choice]}")
    print(f"Computer choose {images[computer_choice]}")

    if user_choice >= 3 and user_choice < 0:
        print("You typed an invalid number. You lose!")
    # logic: 0 beats 2
    elif computer_choice == 0 and user_choice == 2:
        print("You Lose!")
    elif user_choice == 0 and computer_choice == 2:
        print("You Won!")

    # logic: bigger number wins
    elif user_choice > computer_choice:
        print("You Won!")
    elif computer_choice > user_choice:
        print("You Lose!")
    elif computer_choice == user_choice:
        print("It's a tie!")
