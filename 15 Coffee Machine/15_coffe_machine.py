

# Day 15
#### Coffe Machine ####

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
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

resources_left = resources

total_money = 0

ingredients_needed = True


# Checkear si hay resourses para hacer el pedido
def check_resources_left():
    """ Esta funcion checkea que haya ingredientes para hacer el cafe"""
    global ingredients_needed
    ingredients_needed = True
    water_needed = MENU[choice]["ingredients"]["water"]
    milk_needed = MENU[choice]["ingredients"]["milk"]
    coffee_needed = MENU[choice]["ingredients"]["coffee"]

    if resources_left ["water"] < water_needed:
        print ("Sorry there is not enough water")
        ingredients_needed = False
    if resources_left ["milk"] < milk_needed:
        print("Sorry there is not enough milk")
        ingredients_needed = False
    if resources_left ["coffee"] < coffee_needed:
        print("Sorry there is not enough coffee")
        ingredients_needed = False

    resources_left["water"] = resources_left["water"] - MENU[choice]["ingredients"]["water"]
    resources_left["milk"] = resources_left["milk"] - MENU[choice]["ingredients"]["milk"]
    resources_left["coffee"] = resources_left["coffee"] - MENU[choice]["ingredients"]["coffee"]


# Funcion para pagar:
def pay_amount():
    """ Esta funcion contabiliza el pago """
    coffee_cost = MENU[choice]["cost"]
    print(f"{choice} cost ${coffee_cost}")
    pay = 0
    pennies = int(input( "How many pennies :"))
    nickles = int(input("How many nickles :"))
    dimes = int(input("How many dimes :"))
    quarters = int(input("How many quarters :"))

    pennies_total = pennies * 0.01
    nickles_total = nickles * 0.05
    dimes_total = dimes * 0.10
    quarters_total = quarters * 0.25

    pay += pennies_total + nickles_total + dimes_total + quarters_total

    return pay


def compare_money(n1, n2):
    """ Esta funcion compara el precio del cafe con lo que se pago y da cambio"""
    global total_money
    if n1 < n2:
        print (f"Sorry that's not enough money. Money refunded.{pay_amount()}")

    elif n1 == n2:
        print("Thanks lets prepare your coffee!")
        total_money += MENU[choice]["cost"]
    else:
        resultado = n1 - n2
        change = round(resultado, 2)
        print(f"Thanks lets prepare your coffee! Here is ${change} dollars in change")
        total_money += MENU[choice]["cost"]


def coffee_machine():
    """ Esta es la Funcion principal del programa """

    check_resources_left()
    if ingredients_needed:
        payment = float(pay_amount())
        cost = MENU[choice]["cost"]
        compare_money(payment, cost)


# Aca arranca la ejecucion!!!!
machine_on = True
while machine_on:
    choice = str(input("What would you like? (espresso/latte/cappuccino): ").lower())
    report = f"water = {resources_left["water"]}\nmilk = {resources_left["milk"]}\ncoffee = {resources_left["coffee"]} \nmoney = {total_money}"
    if choice == "report":
        print(report)
    elif choice == "off":
        print ("Good Bye!!!")
        machine_on = False
    else:
     coffee_machine()
