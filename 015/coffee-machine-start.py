MENU = {
    "espresso": {
        "ingredients": {
            "water": {"quantity": 50, "unit": "ml"},
            "coffee": {"quantity": 18, "unit": "g"}
        },
        "cost": 150,
        "available": False
    },
    "latte": {
        "ingredients": {
            "water": {"quantity": 200, "unit": "ml"},
            "milk": {"quantity": 150, "unit": "ml"},
            "coffee": {"quantity": 24, "unit": "g"}
        },
        "cost": 250,
        "available": False
    },
    "cappuccino": {
        "ingredients": {
            "water": {"quantity": 250, "unit": "ml"},
            "milk": {"quantity": 100, "unit": "ml"},
            "coffee": {"quantity": 24, "unit": "g"}
        },
        "cost": 300,
        "available": False
    }
}

resources = {
    "water": {"quantity": 300, "unit": "ml"},
    "milk": {"quantity": 200,  "unit": "ml"},
    "coffee": {"quantity": 100, "unit": "g"}
}

cash = {
    "quarters": {"inserted": 0, "present": 0, "value": 25},
    "dimes": {"inserted": 0, "present": 0, "value": 10},
    "nickles": {"inserted": 0, "present": 0, "value": 5},
    "pennies": {"inserted": 0, "present": 0, "value": 1}
}


def print_resources_report():
    """Display Coffee machine stock content"""
    print(f"\nResources present in Coffee Machine")
    for resource in resources:
        name = resource.capitalize()
        quantity = resources[resource]['quantity']
        unit = resources[resource]['unit']
        print(f"{name}: {quantity}{unit}")


def print_cash_report(bucket="present"):
    """Display content of cash bucket present/inserted"""
    print(f"\nCash in bucket {bucket} of Coffee Machine")
    total_amount = 0
    if bucket not in ("present", "inserted"):
        bucket = "present"
    for coin in cash:
        unit = cash[coin][bucket]
        value = round(cash[coin]["value"]/100, 2)
        total_amount += unit * value
        print(f"{coin}: ({unit} * {value}) = ${unit * value}")
    print("Total amount:\t $", round(total_amount, 2))


def is_available(product):
    """Verify if Coffee Machine can distribute product"""
    MENU[product]["available"] = True
    for ingredient in MENU[product]["ingredients"]:
        quantity = MENU[product]["ingredients"][ingredient]["quantity"]
        if quantity > resources[ingredient]["quantity"]:
            MENU[product]["available"] = False
    return MENU[product]["available"]


def check_available_products():
    """Return all available products in coffee machine"""
    available = []
    for item in MENU:
        if is_available(item):
            available.append(item)
    return available


def ask_int(text,default=0):
    try:
        answer = int(input(text))
    except ValueError:
        answer = 0
    return answer


def money_ask_change():
    print("Please insert coins.")
    change_inserted = 0
    for key in cash:
        nb_coin = ask_int(f"How many {key}?: ")
        cash[key]["inserted"] = nb_coin
        change_inserted += cash[key]["value"] * nb_coin
    return change_inserted


def is_enough_change(asked_product, amount):
    if MENU[asked_product]["cost"] <= amount:
        return True
    else:
        return False


def return_money():
    """Ask to keep change in Coffee Machine for another product"""
    answer = input("Do you want an other product? yes/no ")
    if answer == "yes":
        return False
    else:
        return True


def money_return_inserted():
    """Return all inserted coins and print total amount"""
    print_cash_report("inserted")
    change_inserted = 0
    for key in cash:
        change_inserted += cash[key]["value"] * cash[key]["inserted"]
        cash[key]["inserted"] = 0

    print(f"Take your money back: $", round(change_inserted/100, 2))


def money_give_back_change(asked_product, amount):
    # move all coins in cash
    for coin in cash:
        unit = cash[coin]["inserted"]
        cash[coin]["present"] += unit
        cash[coin]["inserted"] = 0
    amount -= MENU[asked_product]["cost"]
    if amount > 0:
        for coin in cash:
            while amount >= cash[coin]["value"]:
                amount -= cash[coin]["value"]
                cash[coin]["present"] -= 1
                cash[coin]["inserted"] += 1


def distribute(product):
    """Function to distribute product of Coffee Machine"""
    print(f"Enjoy your {product}!")


def stock_deduce_product_content(product):
    """Decrease the ingredients stocks in coffee machine"""
    ingredients = MENU[product]["ingredients"]
    for ingredient in ingredients:
        resources[ingredient]["quantity"] -= ingredients[ingredient]["quantity"]


def main():
    in_service = True

    while in_service:
        # Check all available products in Coffee Machine
        available_products = check_available_products()
        choice = input(f"What would you like {available_products}? ")
        if choice == "help":
            print(f"Available commands: report,off and {available_products}")
        elif choice == "report":
            print_resources_report()
            print_cash_report()
        elif choice == "off":
            in_service = False
        elif choice in available_products:
            if is_available(choice):
                inserted_coins = money_ask_change()
                if is_enough_change(choice,inserted_coins):
                    distribute(choice)
                    stock_deduce_product_content(choice)
                    money_give_back_change(choice,inserted_coins)
                else:
                    print("Sorry that's not enough money. Money refunded.")
                money_return_inserted()
        else:
            print(f"Sorry that's not a correct command! Try again.\n")


if __name__ == '__main__':
    main()
