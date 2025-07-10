from data import MENU, resources
import pprint

is_machine_off = False

water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
money = resources["money"] 


def total_price():
        rupees_10 = int(input('How many 10 rupees notes you have :- ')) * 10
        rupees_20 = int(input('How many 20 rupees notes you have :- ')) * 20
        rupees_50 = int(input('How many 50 rupees notes you have :- ')) * 50
        rupees_100 = int(input('How many 100 rupees notes you have :- ')) * 100

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
        print(f"water : {water}, milk : {milk}, coffee : {coffee}, money : {money}")

    elif user_input in MENU:
        order = MENU[user_input]
        ingredients = MENU[user_input]["ingredients"]
        print(f"Pay {order['cost']}")

        if is_resource_sufficient(ingredients, resources):
            user_price = total_price()

            if user_price >= order["cost"]:
                print(f"Here is your order {user_input} and your change {user_price - order["cost"]}")
                money += order["cost"]
                water -= ingredients["water"]
                coffee -= ingredients["coffee"]

                if ingredients["milk"]:
                 coffee -= ingredients["milk"]

            else:
                print("you don't have enough money")

    else:
        print("Not a valid input. Try again!")
