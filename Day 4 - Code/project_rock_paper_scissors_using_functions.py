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


def print_rock():
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")


def print_paper():
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")


def print_scissors():
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")


computer_choice = random.randint(0, 2)
user_choice = int(input("Choose rock(0), paper(1) or scissors(2): "))

print(f"Computer choose {computer_choice}")
if computer_choice == 0:
    print_rock()
elif computer_choice == 1:
    print_paper()
elif computer_choice == 2:
    print_scissors()

print(f"You choose {user_choice}")
if user_choice == 0:
    print_rock()
elif user_choice == 1:
    print_paper()
elif user_choice == 2:
    print_scissors()


# if computer choose rock
if computer_choice == 0:
    if user_choice == 0:
        print("It's a draw!")
    elif user_choice == 1:
        print("You won!")
    elif user_choice == 2:
        print("You lose!")
    else:
        print("Invalid Choice! You lose")

# if computer choose paper
if computer_choice == 1:
    if user_choice == 1:
        print("It's a draw!")
    elif user_choice == 2:
        print("You won!")
    elif user_choice == 0:
        print("You lose!")
    else:
        print("Invalid Choice! You lose")

# if computer choose scissors
if computer_choice == 2:
    if user_choice == 2:
        print("It's a draw!")
    elif user_choice == 0:
        print("You won!")
    elif user_choice == 1:
        print("You lose!")
    else:
        print("Invalid Choice! You lose")
