import art
profit=0
print(art.logo)

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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def can_make_any_drink():
    for drink in MENU.values():
        possible = True

        for ingredient in drink["ingredients"]:
            if drink["ingredients"][ingredient] > resources[ingredient]:
                possible = False

        if possible:
            return True

    return False

def coins():
    total=0
    print("Please insert coins.")
    total+=int(input("How many quarters: ")) * 0.25
    total+=int(input("How many dimes: ")) * 0.1
    total+=int(input("How many nickles: ")) * 0.05
    total+=int(input("How many pennies: ")) * 0.01
    return total

def resources_sufficient(order_ingredients):
    for ingredients in order_ingredients:
        if order_ingredients[ingredients] > resources[ingredients]:
            print("Sorry, we are out of ingredients!")
            return False
    return True

def check_transaction(money_received,order_amount):
    global profit
    if money_received < order_amount:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    elif money_received == order_amount:
        profit+=order_amount
        return True
    else:
        profit += order_amount
        change=round(money_received-order_amount,2)
        print(f"Here is ${change} dollars in change.")
        return True

def make_coffee(name_of_drink, order_ingredients):
    for each_item in order_ingredients:
        resources[each_item] -= order_ingredients[each_item]
    print(f"Here is your {name_of_drink}. Enjoy☕️☕️☕️!")
    return True

should_continue=True
while should_continue:
    decision=input("What would you like to drink?(espresso/latte/cappuccino): ").lower()
    if decision == "off":
        should_continue=False
    elif decision == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
    elif decision == "profit":
        print(f"Total revenue for today is: ${profit}")
    elif decision not in MENU:
        print("Invalid choice. Please choose espresso, latte, or cappuccino.")
    else:
        drink = MENU[decision]
        if resources_sufficient(drink["ingredients"]):
            payment=coins()
            if check_transaction(payment,drink["cost"]):
                make_coffee(decision, drink["ingredients"])

    if not can_make_any_drink():
        print("The coffee machine has run out of ingredients and cannot make any more drinks.")
        should_continue = False

print("Thank you! Have a good head ahead...!")
