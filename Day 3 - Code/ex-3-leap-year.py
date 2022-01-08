'''
Logic:
EVERY year that is evenly divisible by 4
EXCEPT every year that is evenly divisible by 100
UNLESS every year that is evenly divisible by 400
'''

year = int(input("Enter the year: "))

# firstly check if it is evenly divisible by 4
if(year % 4 == 0):
    # secondly check if it is evenly divisible by 100
    if year % 100 != 0:
        print(f"{year} is a leap year")
        # check if it is divisible by 400
    else:
        if year % 400 == 0:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
else:
    print(f"{year} is not a leap year")
