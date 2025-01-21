from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

option = Menu()
coffee_maker_obj = CoffeeMaker()
money_machine_obj = MoneyMachine()
is_on = True

while is_on:
    try:
        choice = input(f"What would you like? ({option.get_items()}): ").lower()

        if choice == "off":
            is_on = False

        elif choice == "report":
            coffee_maker_obj.report()
            money_machine_obj.report()

        else:
            menu_item = option.find_drink(choice)
            if coffee_maker_obj.is_resource_sufficient(menu_item):
                if money_machine_obj.make_payment(menu_item.cost):
                    coffee_maker_obj.make_coffee(menu_item)

    except AttributeError as err:
        print("Please enter only valid given options.")