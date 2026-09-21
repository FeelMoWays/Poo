MENU = {
    'espresso': {
        'ingredients': {
            'water': 50,
            'coffee': 18
        },
        'cost': 1.5,
    },
    "latte": {
        'ingredients': {
            'water': 200,
            'milk': 150,
            'coffee': 24,
        },
        'cost': 2.5,
    },
    'cappuccino': {
        'ingredients': {
            'water': 250,
            'milk': 100,
            'coffee': 24,
        },
        'cost': 3.0,
    }
}

resources = {
    'water': 300,
    'milk': 200,
    'coffee': 100,
}

machine_is_on = True


def coins():
    total_cost = 0

    total_cost += int(input("How many quarters: ")) * 0.25
    total_cost += int(input("How many dimes: ")) * 0.10
    total_cost += int(input("How many nickels: ")) * 0.05
    total_cost += int(input("How many pennies: ")) * 0.01

    return total_cost


def check(order_ingredients):
    is_enough = True

    for ingredient in order_ingredients:
        if order_ingredients[ingredient] > resources[ingredient]:
            print(f"Sorry, there isn't enough {ingredient}.")
            is_enough = False

    return is_enough


def transaction_successful(user_cost, drink_cost):
    if user_cost < drink_cost:
        return False

    return True


def deduct(order_ingredients):
    for ingredient in order_ingredients:
        resources[ingredient] -= order_ingredients[ingredient]


while machine_is_on:

    choice = input(
        "What would you like? (espresso/latte/cappuccino): "
    ).lower()

    if choice == "off":
        machine_is_on = False

    elif choice == "report":
        print(resources)

    elif choice not in MENU:
        print("Invalid choice.")

    else:
        drink = MENU[choice]

        if check(drink['ingredients']):

            money = coins()

            if transaction_successful(money, drink['cost']):

                change = money - drink['cost']

                print("Transaction successful!")
                print(f"Here is ${change:.2f} in change.")

                deduct(drink['ingredients'])

                print(f"Here is your {choice}. Enjoy!")

            else:
                print("Sorry, that's not enough money. Money refunded.")

