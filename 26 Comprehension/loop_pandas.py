### Para itinerar dentro de un Data Frame de panda
## D26 V10 ##
import pandas

student_dict = {
    "students": ["Angela", "James", "Lily"],
    "score": [56, 76, 98],
}

# Asi creo el Data Frama desde un Dict
student_data_frame = pandas.DataFrame(student_dict)
#   students  score
# 0   Angela     56
# 1    James     76
# 2     Lily     98


##  METODO ITERROWS ##

# Pandas tiene un metodo interno para itinerar entre rows: iterrows()
for(index, row) in student_data_frame.iterrows(): # por cada index con un row..
    # esto va a devolver un "objeto"  y puedo llamar a los diferentes atributos.

    print(row)
    # Devuelve algo asi... por cada row
    # students    Angela
    # score        56

    print(row.students)
    # Angela
    # James
    # Lily

    print (row.score)
    # 56
    # 76
    # 98
