from word_list import word_list
from hangman_art import stages, logo
# from replit import clear
import random
# import os
# os.system('cls')
# There must be 3 levels ie., easy, medium and hard
# in easy mode -> every 2nd letter of word must be displayed
# in medium mode -> every 3rd letter of word must be displayed
# in hard mode -> every 4th letter of word must be displayed
print(logo)
game_end = False
lives = 6  # to keep track of lives
# word_list = ["pytorch", "pandas", "tkinter", "tenserflow", "django", "flask"]
# this will choose a random word from word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Testing code
# print(f'Pssst, the solution is {chosen_word}.')

display = []
# For each letter in the chosen_word, add a "_" to 'display'.
for letter in range(word_length):
    display += "_"
print(display)
# So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

while not game_end:
    guess = input("Guess a letter: ").lower()
    # clear()
    # check if letter already exists
    if guess in display:
        print(f"You've already guessed {guess}")
    # If the letter at that position matches 'guess' then reveal that letter in the display at that position.
    for position in range(word_length):
        # if guess matches any letter in chosen_word
        if chosen_word[position] == guess:
            # replace that '_' with that letter
            display[position] = guess

    if guess not in chosen_word:
        # reduce lives by 1
        print(f"You guessed {guess}, that's not in the word. You lost a life.")
        lives -= 1
        print(stages[lives])
        # os.system('cls')
        if lives == 0:
            game_end = True
            print("You've been hanged\nYou lose!")

    # convertion to string
    print(f" ".join(display))
    # when there are no more '-' in display list, game_end and user wins
    if '_' not in display:
        game_end = True
        print("You won!")
