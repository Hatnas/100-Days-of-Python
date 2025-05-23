
### DICT COMPREHENSION ###
# Permite crear un Dict con solo una lina
# new_dict = {key_name: key_value for item in list}
import random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Frank"]
students_score = {student: random.randint(1,100) for student in names}

# Tambien puedo crear un Dict de otro Dict
# new_dict = {key_name: key_value for (key,value) in dict.items()}

stud_dict_from_dict ={student : score for (student,score) in students_score.items()}

# CONDITION DICT COMPREHENSION
# Puedo agregarle una condicion
# new_dict = {key_name: key_value for (key,value) in dict.items() if test}
# Aca armo un Dict con los alumnos que tubieron mas de 60
passed_student ={student : score for (student,score) in students_score.items() if score >= 60}


### Para crear un dict que tenga las palabras y su cantidad de letras
phrase = "What is the Airspeed Velocity of an Unladen Swallow"
result = {word:len(word) for word in phrase.split()}  # uso split() para seprar por palabra

print (result)
# {'What': 4,
# 'is': 2,
# 'the': 3,
# 'Airspeed': 8,
# 'Velocity': 8,
# 'of': 2,
# 'an': 2,
# 'Unladen': 7,
# 'Swallow': 7}