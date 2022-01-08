from art import logo
import os


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def remainder(a, b):
    return a % b


# in dicts, no need to add parenthesis at end of functions
operators = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
    '%': remainder,
}


def calculator():
    print(logo)
    a = float(input("Enter the first number: "))
    for symbol in operators:
        print(symbol)
    while True:
        op = input("Pick an operation: ")
        b = float(input("Enter the next number: "))
        # storing specified function in func
        func = operators[op]
        # now func is our new req function, we can pass arguments to it
        answer = func(a, b)
        print(f"{a} {op} {b} = {answer}")
        is_continue = input(
            f"Type 'y' to continue calculating with {answer}, or type 'n' to reset, or type 'e' to exit: ")
        if is_continue == 'e':
            break
        elif is_continue == 'y':
            a = answer
        elif is_continue == 'n':
            def clear():
                return os.system('cls')
            clear()
            calculator()
        else:
            print("INVALID CHOICE\n\tPROGRAM EXIT")
            break


calculator()

'''
this is an alternative method
if op == '+':
    print(f"{a} {op} {b} = {add(a, b)}")
elif op == '-':
    print(f"{a} {op} {b} = {subtract(a, b)}")
elif op == '*':
    print(f"{a} {op} {b} = {multiply(a, b)}")
elif op == '/':
    print(f"{a} {op} {b} = {divide(a, b)}")
elif op == '%':
    print(f"{a} {op} {b} = {remainder(a, b)}")
'''
