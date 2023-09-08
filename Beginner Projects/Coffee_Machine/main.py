MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
turn_off_machine = False
money = 0.0


def machine_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${round(money, 2)}")
    return


def making_the_coffee(water, coffee, milk, income, cost, coffee_name):
    resources["water"] -= water
    resources["coffee"] -= coffee
    resources["milk"] -= milk
    global money
    money += cost
    refund = income - cost
    print(f'Here is ${round(refund, 2)} in change')
    print(f"Here is your {coffee_name} ☕. Enjoy")


def is_enough_resources(responses):
    water = MENU[responses]["ingredients"]["water"]
    coffee = MENU[responses]["ingredients"]["coffee"]
    cost = MENU[responses]["cost"]
    milk = MENU[responses]["ingredients"]["milk"]

    if water > resources['water']:
        print("Sorry there is not enough water. Money refunded.")
    elif coffee > resources['coffee']:
        print("Sorry there is not enough coffee. Money refunded.")
    elif milk > resources['milk']:
        print("Sorry there is not enough milk. Money refunded.")
    else:
        total_insert_coins = insert_coins()

        if total_insert_coins < cost:
            print("Sorry that's not enough money. Money refunded.")
        else:
            making_the_coffee(water, coffee, milk, total_insert_coins, cost, responses)
    return


def insert_coins():
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    return 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies


while not turn_off_machine:
    response = (input("What would you like? (espresso/latte/cappuccino):")).lower()

    if response == 'off':
        turn_off_machine = True
    elif response == 'report':
        machine_report()
    elif response == 'espresso' or response == 'latte' or response == 'cappuccino':
        is_enough_resources(response)
    else:
        print(f"Invalid input, please re-enter your choice. ")
