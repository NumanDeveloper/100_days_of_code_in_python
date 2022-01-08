print("----- Welcome to the RollerCoaster -----")

bill = 0
height = int(input("What's your height in cm: "))
if (height) > 120:
    print("Congrats! You can ride the rollercoaster!")
    age = int(input("What's your age: "))
    if(age < 12):
        bill = 5
        print("Children ticket is $5")
    elif(age <= 18):
        bill = 7
        print("Youth ticket is $7")
    elif(age >= 45 and age <= 55):
        print("Everything is going to be ok. Have a free ride with us")
    else:
        bill = 12
        print("Adult ticket is $12")
    photo = input("Do you want a photo taken? yes(y) or no(n): ")
    if photo == 'y':
        bill += 3

    print(f"Your final bill is ${bill}")
else:
    print("Sorry! You've to grow taller before you can ride.")
