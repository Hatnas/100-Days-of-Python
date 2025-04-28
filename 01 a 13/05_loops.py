
# Averange Height

student_height = input().split()   # Creo una lista, .split() hace que cada dato separado por un espacio sea un "elemento" diferente
for n in range(0, len(student_height)): # Aca marco el rango y nombro "n" a los elementos de la lista. Para pasar por ellos
    student_height[n] = int(student_height[n]) # Transformo los elementos del la lista en Int. Uno por uno


total_height = 0  #Creo una variable con valor = 0. Para ir sumandole los "elementos" que llamaremos "height"

for height in student_height:
    total_height += height

print (f"Total Height =", total_height)
print (f"Number of students =", len(student_height))
print (f"Average heigh = {total_height // int(len(student_height))}")



# High Score

student_score = input().split()   
for n in range(0, len(student_score)):
    student_score[n] = int(student_score[n]) 

high_score = 0

for score in student_score:
    if high_score < score:
        high_score = score
    else:
        high_score = high_score

print(f"the Hig Score is {high_score}")


# For Loops with Range
for number in range (1, 10):  # Determina el Rango (x, y) desde x hasta y. Pero y no esta incluido
    print (number)


# Adding even number (006)
target = int(input())
total = 0

for number in range (2, target + 1, 2):  
    total += number

print (total)


# Fizz Buzz (007)
target = int(input())
for number in range (1, target + 1):  
    if number % 3 == 0 and number % 5 == 0:
        print ("FizzBuzz")
    elif number % 3 == 0:
        print ("Fizz")
    elif number % 5 == 0:
        print ("Buzz")
    else:
        print (number)



### Py Password Generator (008)  ###
import random

letters = ["a", "b", "c", "d", "e"]
numbers =["1", "2", "3", "4", "5"]
signs = ["!", "#", "$", "(", ")"]

print ("Welcome to the Password Generator")

nr_letters = int(input("How many letters\n"))
nr_numbers = int(input("How many numbers\n"))
nr_signs = int(input("how many sings\n"))

# Easy
"""
password = ""
for char in range(1, nr_letters + 1):
    password += random.choice(letters)

for num in range(1, nr_numbers + 1):
    password += random.choice(numbers)
    
for sig in range(1, nr_signs +1):
    password += str(random.choice(signs))

print(password)
"""

# Hard (008)
password_list = []              # Creo una lista vacia
for char in range(1, nr_letters + 1):
    password_list += random.choice(letters)  # Agrego valores aleatores de otras listas

for num in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)
    
for sig in range(1, nr_signs +1):
    password_list += str(random.choice(signs))


random.shuffle(password_list)       # Mezclo los valores de la lista 

password = ""                       # Creo un Str vacio
for char in password_list:
    password += char                # Voy sumando los valores al str

print (password) 


