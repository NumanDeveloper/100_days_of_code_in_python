
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_enough_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f'Sorry, there is not enough {item}')
            return False
    return True


def process_coins():
    print("Insert the coins.")
    total = int(input("How many quaters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickes?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_given, drink_cost):
    '''Returns true if there is enough money, else return false'''
    # if money_given greater than drink_cost, transaction successful
    if money_given >= drink_cost:
        change = round((money_given - drink_cost), 2)
        print(f"Here's the ${change} in change.")
        return True
    else:
        print("Sorry, there's not enough money! Money refunded")
        return False


def make_coffee(drink_name, order_ingredients):
    '''Deduct the req ingredients from resources'''
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}☕. Enjoy")


is_on = True
while is_on:
    choice = input(
        "What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_enough_resources(drink['ingredients']):
            # if resources are enough, ask for payment
            payment = process_coins()
            # check if the transaction successful
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])
