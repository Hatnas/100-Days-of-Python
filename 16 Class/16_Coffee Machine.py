### Coffee Machine oop Version ###

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffe_maker = CoffeeMaker()
money_machine = MoneyMachine()
is_on = True


while is_on:
    options = menu.get_items()
    choice = input(f"What would you like ({options})? ")  # aca genero el input como "choice"
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffe_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice) # Aca paso el input como un MenuItem dentro de Menu
        if coffe_maker.is_resource_sufficient(drink):
            print (f"Its ${drink.cost}")

            if money_machine.make_payment(drink.cost):
                coffe_maker.make_coffee(drink)



