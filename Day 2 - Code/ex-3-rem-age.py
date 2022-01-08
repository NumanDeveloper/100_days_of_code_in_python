'''
Logic:
1. Take age
2. Calculate the remaining days, weeks, months left out of 90 years
'''

assumedAge = 90
currentAge = int(input("What's your current age: "))
remainingAge = assumedAge - currentAge
months = remainingAge*12
weeks = remainingAge*52
days = remainingAge*365

message = f"You have {days} days, {weeks} weeks and {months} months left."
print(message)
