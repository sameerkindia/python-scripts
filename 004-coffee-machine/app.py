from data import MENU, resources
import pprint

is_machine_off = False

# Use resources dictionary directly to manage available resources
water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
# This is just a separate variable, we need to update resources["money"]
money = resources["money"]


def total_price():
    try:
        rupees_10 = int(input('How many 10 rupees notes you have :- ')) * 10
        rupees_20 = int(input('How many 20 rupees notes you have :- ')) * 20
        rupees_50 = int(input('How many 50 rupees notes you have :- ')) * 50
        rupees_100 = int(input('How many 100 rupees notes you have :- ')) * 100
    except ValueError:
        print("Please enter a valid number.")
        return 0
    total_rupees = rupees_10 + rupees_20 + rupees_50 + rupees_100
    return total_rupees


def is_resource_sufficient(order_ingredients, resources):
    for item in order_ingredients:
        if item not in resources or resources[item] < order_ingredients[item]:
            print(f"Sorry, not enough {item}.")
            return False
    return True


while not is_machine_off:
    user_input = input(
        "What would you like? (espresso/latte/cappuccino) :- ").lower()

    if user_input == 'off':
        is_machine_off = True

    elif user_input == 'report':
        # Print current resource states including money from resources
        print(
            f"water : {resources['water']}, milk : {resources['milk']}, coffee : {resources['coffee']}, money : {resources['money']}")

    elif user_input in MENU:
        order = MENU[user_input]
        ingredients = order["ingredients"]
        print(f"Pay {order['cost']}")

        if is_resource_sufficient(ingredients, resources):
            user_price = total_price()

            if user_price >= order["cost"]:
                change = user_price - order["cost"]
                print(
                    f"Here is your order {user_input} and your change {change}")

                # Add the cost to resources["money"]
                resources["money"] += order["cost"]

                # Subtract the ingredients used
                resources["water"] -= ingredients["water"]
                resources["coffee"] -= ingredients["coffee"]
                if "milk" in ingredients:
                    resources["milk"] -= ingredients["milk"]

            else:
                print("You don't have enough money.")

    else:
        print("Not a valid input. Try again!")
