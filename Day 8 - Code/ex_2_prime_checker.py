# Write your code below this line 👇
def prime_checker(number):
    prime = True
    for divisor in range(2, number):
        if number % divisor == 0:
            prime = False
            # print(f"{number} isn't a prime number")
            break  # will prevent extra iterations
    if prime:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} isn't a prime number.")


# Write your code above this line 👆
# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
