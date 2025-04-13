from Resources import resources
from Resources import MENU


def report():
    print(f'Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}g')
    # print(f"Money: {}")


def resources_check(selection):
    """Checks the coffee machine has the available resource for chosen selection"""
    for resource in selection:
        if resources[resource] - selection.get(resource) > 0:
            enough = True
            # print(f"There is enough {resource}!")
        else:
            # print(f"Not enough {resource}!")
            return False, resource
    return True, resource
    # variable may be referenced before assignment,
    # should assign another variable to resource as this is local scope


def cash_input(drink):
    """Prompts the user to input cash and totals, """
    cost = MENU[drink]["cost"]
    print("Please insert coins")
    print(f"A {drink.capitalize()} costs: ${cost}")
    quarters = int(input("How many quarters?"))  # Could place these into a list and use for loop
    dimes = int(input("How many dimes?"))
    nickels = int(input("How many nickels"))
    pennies = int(input("How many pennies?"))
    # Improvement to prevent code failing when non int is entered could be done here.
    total = (quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01)
    total2 = total
    # Additional user improvement for when the input coins are not enough, room here to remove redundant code
    while cost > total2:
        print(f"not enough, please insert ${round(cost - total2, 2)}")
        quarters = int(input("How many quarters?"))
        dimes = int(input("How many dimes?"))
        nickels = int(input("How many nickels"))
        pennies = int(input("How many pennies?"))
        total2 += (quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01)
    print(f"Dispensing ${float("{:.2f}".format(total2 - cost))} in change...")


def remove_resources(drink):
    """Removes the resources from coffee machine after dispensed"""
    for resource in drink:
        remaining = resources[resource] - drink.get(resource)
        resources[resource] = remaining


def coffee_machine():
    complete = False
    while not complete:
        user_choice = input(f"What would you like? (espresso/latte/cappuccino): ").lower()
        if user_choice in MENU:
            ingredient_of_drink = MENU[user_choice]["ingredients"]
            check = resources_check(ingredient_of_drink)
            if not check[0]:
                print(f"Sorry there is not enough {check[1]}! Please refill.")
            else:
                cash_input(user_choice)
                remove_resources(ingredient_of_drink)
                print(f"Here is your {user_choice} Enjoy!")
        elif user_choice == "report":
            report()
        else:
            print("Invalid input")


print(coffee_machine())
