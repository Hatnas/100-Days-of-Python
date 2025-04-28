
# Day 9 

# Dictionaries and Nesting

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
}


# De este forma llamo al Valor correspondiente a la Key "Bug"
print (programming_dictionary["Bug"])      

# Agregando nuevos items al diccionario
programming_dictionary["Loop"] = "The action of doing something over and over again" 

# Borrar un diccionario entero / crear un diccionario
empty_dictionary = {}
    # si empty_dictionary hubiese tenido algo adentro, Ahora estaria completamente en vacio

# Editar un diccionario
programming_dictionary["Bug"] = "Lo que tenga ganas"  # De esta forma Sobreescribo lo que contiene "Bug"

# Loop through a dictionary
for key in programming_dictionary:
    print (key)                    #  Esto solo me va a dar las Key que estan en el Dict.
    print (programming_dictionary[key]) # Esto me va a devolver solo el Value de la Key correspondiente



# 003

student_score = {
    "Harry": 81,
    "Ron": 78,
    "Hermaioni": 99,
    "Draco": 74,
    "Neville": 62,
}

students_grades = {}

for student in student_score:
    score = student_score[student]
    if score >90:                     # crea un elemento dentro de studente_grade tomando la key que esta pasando y dandole un value
        students_grades[student] = "Outstanding"
    elif score >80:
        students_grades[student] = "Exceeds expectations"
    elif score >70:
        students_grades[student] = "Acceptable"
    else:
        students_grades[student] = "Fail"

print (students_grades)


# 004
# Nesting Lists and Dict

 # Nesting Lists into Dict
travel_log = {
    "France": {"cities_visited":["Paris", "Lille", "Dijon"], "total_visits": 0},
    "key2": {
        "nested key 1:":"value 1", 
        "nested key 2": "value 2", 
        "nested key 3": "value 3",
        },
    "Germany": ["Berlin", "Hamburg", "Stuttgard"],
}

print (travel_log["Germany"][0])  # de esta forma se llama al elemento dentro de la lista "Berlin"

# Nesting Dict into Lists

travel_log = [
    {
        "country": "France",
        "cities_visited":["Paris", "Lille", "Dijon"],
        "total_visits": 0,
    },  
    {
        "country":"Germany", 
        "cities_visited" : ["Berlin", "Hamburg", "Stuttgard"], 
        "total_visits": 0
    }
]


# 005

# Ejercicio
# https://app.auditorium.ai/lesson/eelyNMYJKXeNJAbjssSEQz0m88XvnhX6/58076521-a623-49e9-8d55-7a0c76c60464?sl=%22ee33719e-7ebe-4e83-aafa-fabf7184a81b%22&st=%22eaddaad3-4d91-4dcc-a6a1-d559022fe042%22

# mi respuesta
def add_new_country(country, visits, list_of_cities):
    travel_log.append({
        "country" : country,
        "visits": visits,
        "cities" : list_of_cities,
    })

# la respuesta de la profesora:
def add_new_country(name, times_visited, cities_visited):
  new_country = {}
  new_country["country"] = name
  new_country["visits"] = times_visited
  new_country["cities"] = cities_visited
  travel_log.append(new_country)


# 007 
## Secret bidd not so secret

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''


buyer_dict = {}


def find_higest_bidder():
    highest_bid = 0
    winner = ""
    for bidder in buyer_dict:
        bid_amount = buyer_dict[bidder]
        if bid_amount> highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print (f"The winner is: {winner}, Whit a bid of {highest_bid}!")


another_buyer = True
print (logo) 
while another_buyer == True:
    name = input("What is your name? ")
    amount = int(input("What is your bid? $"))
    buyer_dict[name]= amount
    any_other = input("Is there any other bidder? Type 'yes' or 'no'. ").lower()
    if any_other == "yes":
        # clear() pero no se como
        another_buyer = True
    else:
        # clear() pero no se como
        another_buyer = False
        find_higest_bidder()


