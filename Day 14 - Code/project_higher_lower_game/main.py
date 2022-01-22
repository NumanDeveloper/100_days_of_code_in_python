import os
from art import logo, vs
from game_data import data
import random


def clear():
    os.system("cls")


def format_string(account):
    '''It'll take account dict and return formatted string'''
    name = account['name']
    desc = account['description']
    country = account['country']
    return f"{name}, a {desc}, from {country}."


def compare(guess, follower_a, follower_b):
    if follower_a > follower_b and guess == 'a':
        return True
    elif follower_a < follower_b and guess == 'b':
        return True
    else:
        return False


def run_game():
    print(logo)
    final_score = 0
    game_end = False
    acount_b = random.choice(data)
    while not game_end:
        # a random dict will be stored in choice
        acount_a = acount_b
        acount_b = random.choice(data)
        if acount_a == acount_b:
            acount_b = random.choice(data)
        follower_a = acount_a['follower_count']
        follower_b = acount_b['follower_count']
        print(f'Compare A: {format_string(acount_a)}')
        print(vs)
        print(f'Against B: {format_string(acount_b)}')
        guess = input(
            "Who has more INSTAGRAM followers? Type A or B: ").lower()
        clear()

        is_win = compare(guess, follower_a, follower_b)
        if is_win:
            final_score += 1
            print(f"\nYou are right! Current Score: {final_score}.")
        else:
            # clear()
            print(
                f"\nSorry, You guessed it wrong!\nYou scored {final_score} points.")
            game_end = True


# calling the game function to run the game
run_game()