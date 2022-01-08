# Logic
# if number is divisible by 3, print 'Fizz'
# if number is divisible by 5, print 'Buzz'
# if number is divisible by 15, print 'FizzBuzz'

for number in range(1, 101):
    # caution: this condition should be checked at first
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
