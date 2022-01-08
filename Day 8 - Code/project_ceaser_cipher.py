from art import logo
# i have added the alphabets twice, bcz if my index exceeds 25, it will again start from 0
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)


def caeser(start_text, shift, direction):
    end_text = ""  # will store encoded text
    if direction == 'decode':
        shift *= -1
    for char in start_text:  # looping through eact element, letter reps each letter, not index
        if char in alphabet:
            # gives index of current letter in alphabet list
            position = alphabet.index(char)
            new_position = position + shift
            # adds new letter in end_text str
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"The {direction}d text is {end_text}")


should_continue = True
while should_continue == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 25  # shift between 0 and 25

    # caeser function call
    caeser(text, shift, direction)

    result = input("Type 'yes' to continue and 'no' to exit: ")
    if result == 'no':
        should_continue == False
        print("Good Bye!")
        break
