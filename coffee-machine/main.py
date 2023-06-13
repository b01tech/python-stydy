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
    },
}

resource = {"water": 300, "milk": 300, "coffee": 100, "money": 0}


def pay(total, product_cost, command):
    change = round(total - product_cost, 2)
    resource["money"] += product_cost
    print(f"Here is ${change} in change.")
    print(f"Here is your {command}. Enjoy!")


def consume(command):
    for prod in resource:
        if prod != "money":
            resource[prod] -= MENU[command]["ingredients"][prod]


def check_resource(command):
    for prod in resource:
        if prod != "money":
            if resource[prod] < MENU[command]["ingredients"][prod]:
                return [True, prod]
            else:
                return [False]


def payment(command):
    quarters = int(input("How many quarters?  "))
    dimes = int(input("How many dimes?  "))
    nickles = int(input("How many nickles?  "))
    pennies = int(input("How many pennies?  "))
    total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    product_cost = MENU[command]["cost"]
    if product_cost > total:
        print(total)
        print("Sorry that's not enough money. Money refunded")
        start()
    elif check_resource(command)[0]:
        print(f"There is not {check_resource(command)[1]} enough. Sorry!")
        start()
    else:
        consume(command)
        pay(total, product_cost, command)
        start()


def start():
    command = input("What would you like? (espresso/latte/cappuccino): ")
    if command == "report":
        print(
            f"Water:{resource['water']}ml\nMilk:{resource['milk']}ml\nCoffee:{resource['coffee']}g\nMoney:${resource['money']}\n"
        )
        start()
    elif command == "espresso" or command == "latte" or command == "cappuccino":
        payment(command=command)
    else:
        print("Input invalid.")
        start()


# total = 0
start()
