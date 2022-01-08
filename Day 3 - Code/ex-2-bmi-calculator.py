'''
Making a BMI calculator. It takes weight in kg and height in metre and calculate bmi
it also tell about your health condition

Logic:
Calculate the BMI using the formula weight/(height**2)
Check the condition of health using conditionals
'''

# Taking user input
# name = input("Enter your good name: ")
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your hieght in meters: "))

# Calculating BMI
BMI = round(weight/(height**2))

# Checking condition of health
if BMI < 18.5:
    # print(f"Dear {name}")
    print(f"Your bmi is {BMI}, you are underweight.")

elif BMI < 25:
    # print(f"Dear {name}")
    print(f"Your bmi is {BMI}, you are a normal weight.")

elif BMI < 30:
    # print(f"Dear {name}")
    print(f"Your bmi is {BMI}, you are overweight.")

elif BMI < 35:
    # print(f"Dear {name}")
    print(f"Your bmi is {BMI}, you are obese.")

else:
    # print(f"Dear {name}")
    print(f"Your bmi is {BMI}, you are clinically obese.")
