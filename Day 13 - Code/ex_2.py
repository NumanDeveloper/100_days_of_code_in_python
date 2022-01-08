'''Leap year or not'''

year = int(input("Type year to check: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is leap year!")
        else:
            print(f"{year} isn't leap year!")
    else:
        print(f"{year} is a leap year!")
else:
    print(f"{year} isn't a leap year!")
