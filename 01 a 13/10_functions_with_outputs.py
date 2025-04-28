
### 010 Functions with outputs

# 002
def format_name(f_name, l_name):
    formated_f_name = f_name.title()         # .title() tiene un return que puedo guardar dentro de una variable
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"
    

print (format_name("leo", "mastrangelo"))


# 003
# Multiple return values
def format_name (f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid imputs"  # el poner un "return" marco el final de la funcion y sale de la misma
    formated_f_name = f_name.title()         
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"
    

print (format_name(input("What is your first name?: "), input("What is your last name?: ")))


# 004
# respuesta

# 004
def is_leap(year):
    leap = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
        else:
            leap = True
    return (leap)

def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
  if (is_leap(year)) == True:
    month_days[1] = 29
  return (month_days[month -1])

year = int(input()) 
month = int(input()) 
days = days_in_month(year, month)
print(days)


# 005 
## Docstrings ##
# El Docstring es un pequeño texto que explica que hace la funcion o el elemento, Se escribe entre """

def format_name (f_name, l_name):
    """ Esta funcion pone la primer letra de cada palabra en Mayuscula y el resto en minusculas"""  # Docstring
    if f_name == "" or l_name == "":
        return "You didn't provide valid imputs"  
    formated_f_name = f_name.title()         
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"
    
print (format_name(input("What is your first name?: "), input("What is your last name?: ")))


# 010
              ### Calculator ###
logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


def add(n1,n2):
    return n1 + n2
def substract (n1, n2):
    return n1 - n2
def multiply (n1, n2):
    return n1 * n2
def divide (n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print (logo)
    num1 = float(input("what's the first number?: "))

    should_continue = True

    while should_continue == True:
        for symbol in operations:
            print (symbol)
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("what's the next number?: "))
        calculation_function = operations[operation_symbol]  # Tuve que crear una funcion para poder establecer los argumentos
        answer = calculation_function(num1, num2) # Establezco los argumentos de la funcion (que es la citada dentro del Dict)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        continue_calculating = input(f"type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
        if continue_calculating == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()
        
