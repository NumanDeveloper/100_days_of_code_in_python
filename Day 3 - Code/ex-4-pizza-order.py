print("----- Welcome to python pizza diliveries! -----")
size = input("What size pizza do you want? s, m or l: ")
add_papperoni = input("Do you want pepperoni? y or n: ")
extra_cheese = input("Do you want extra cheese? y or n: ")

# first calculate bill
bill = 0
if size == 's':
    bill += 15
elif size == 'm':
    bill += 20
elif size == 'l':
    bill += 25

# if papperoni is added
if add_papperoni == 'y':
    if size == 's':
        bill += 2
    elif size == 'm' or size == 'l':
        bill += 3

# if extra cheese is added
if extra_cheese == 'y':
    bill += 1

print(f"Your final bill is ${bill}")
