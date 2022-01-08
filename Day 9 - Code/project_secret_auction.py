import os
# from replit import clear
# HINT: You can call clear() to clear the output in the console.
from art import logo
record = {}  # for storing bid record

# function for max bid


def max_bid(record):
    max_value = 0
    for bidder in record:
        bid_value = record[bidder]
        if bid_value > max_value:
            max_value = bid_value
            winner = bidder
    print(f"The winner is {winner} with the bid ${max_value}")


print(logo)
print("Welcome to the blind auction")
while True:
    name = input("Enter your name: ")
    bid = int(input("Enter your bid: "))
    record[name] = bid
    # print(record)
    others = input("Anyone else want to bid? yes or no\n")
    if others == 'no':
        break

    def clear(): return os.system('cls')  # on Windows System
    clear()
# function call outside the while loop
max_bid(record)
