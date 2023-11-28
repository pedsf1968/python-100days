from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def main():
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    in_service = True

    while in_service:
        # Check all available products in Coffee Machine
        available_products = menu.get_items()
        choice = input(f"What would you like {available_products}? ")
        if choice == "help":
            print(f"Available commands: report,off and {available_products}")
        elif choice == "report":
            coffee_maker.report()
            money_machine.report()
        elif choice == "off":
            in_service = False
        elif choice in available_products:
            order = menu.find_drink(choice)
            if coffee_maker.is_resource_sufficient(order) and money_machine.make_payment(order.cost):
                coffee_maker.make_coffee(order)
            else:
                print("Sorry that's not enough money. Money refunded.")

        else:
            print(f"Sorry that's not a correct command! Try again.\n")


if __name__ == '__main__':
    main()