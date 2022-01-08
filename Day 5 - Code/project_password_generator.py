# Steps
# number of alphabets in password
# number of digits in password
# number of special_characters in password
# store all in password list
# shuffle the list
# convert list into string

import string  # for populating alphabets and digits
import random  # for randomization

# import alphabets
alphabets = list(string.ascii_letters)
# import digits
digits = list(string.digits)
special_characters = list("!@#$%^&*_-+")
# putting it all together
characters = list(alphabets + digits + special_characters)


def generate_password():
    length = int(input("Enter the length of password: "))
    alphabets_count = int(input("Enter alphabets count in password: "))
    digits_count = int(input("Enter digits count in password: "))
    special_characters_count = int(
        input("Enter special characters count in password: "))
    characters_count = alphabets_count + digits_count + special_characters_count
    # empty list to store password
    password = []
    for i in range(alphabets_count):
        # chose automatically from alphabets list
        password.append(random.choice(alphabets))

    for i in range(digits_count):
        password.append(random.choice(digits))

    for i in range(special_characters_count):
        password.append(random.choice(special_characters))

    if characters_count < length:
        for i in range(length - characters_count):
            password.append(random.choice(characters))

    # shuffling the resultant password
    random.shuffle(password)
    # converting password list into a string using join method
    password_string = "".join(password)
    print(f"Your password is {password_string}")


generate_password()
