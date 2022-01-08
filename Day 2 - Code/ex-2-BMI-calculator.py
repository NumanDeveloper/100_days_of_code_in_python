'''
Logic:
1. Take weight in kg
2. Take height in m
3. Use formula BMI = weight/height**2
'''

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))
# To limit the float value to specific decimal places, you have to use the format() or round() function.
BMI = weight/(height**2)

# print(f"Your BMI is {format(BMI, '.2f')}")
print(f"Your BMI is {round(BMI, 2)}")
