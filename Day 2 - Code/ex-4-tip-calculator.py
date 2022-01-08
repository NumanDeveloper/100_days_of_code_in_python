'''
Logic:
1. Take amount of Bill
2. Take %age tip
3. Between how many people to split the bill
4. Print each people's bill
'''

print("***** Welcome to the tip calculator *****")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

bill_with_tip = bill + (bill * tip / 100)
bill_per_people = round(bill_with_tip/people, 2)

print(f"Each person should pay: ${bill_per_people}")
