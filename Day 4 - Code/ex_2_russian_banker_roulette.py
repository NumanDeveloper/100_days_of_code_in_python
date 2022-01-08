import random

names = input("Give me everybody's names separated by a comma, and space \n")
names_list = names.split(", ")
n = len(names_list)
random_no = random.randint(0, n-1)  # bcz index is 1 less than length
print(f"{names_list[random_no]} will pay the bill")
