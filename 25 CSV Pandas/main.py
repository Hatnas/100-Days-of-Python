### Day 25 CSV Comma Separated Value ###

# with open("weather_data.csv", "r") as doc:
#     data = doc.readlines()
#
# print (data)

# otra forma de abrirlo y que nos quede más comodo es importando csv

# import csv

# with open("weather_data.csv", "r") as doc:
#     data = csv.reader(doc)   # de esta forma creo un objeto csv
#     # for row in data:
#     #     print(row)  # asi nos muestra linea por linea
#     #      # ['day', 'temp', 'condition']
#     #     # ['Monday', '12', 'Sunny']
#     #     # ['Tuesday', '14', 'Rain']
#     #     # ['Wednesday', '15', 'Rain']
#     #     # ['Thursday', '14', 'Cloudy']
#     #     # ['Friday', '21', 'Sunny']
#     #     # ['Saturday', '22', 'Sunny']
#     #     # ['Sunday', '24', 'Sunny']
#
#     # Ahora vamos a hacer una lista de las temperaturas como int
#     #
#     # temperature = []
#     # for row in data:
#     #     if row[1] != "temp":
#     #         temperature.append (int(row[1]))
#     # print (temperature)
#


##  PANDAS ##
# https://pandas.pydata.org/docs/

import pandas

# nos abre el csv como una tabla directamente con cada linea numerada
data = pandas.read_csv("weather_data.cs")
print (data)


# para poder tener solo las temperaturas tengo que pedirle lo que esta en la columna "temp"
print (data["temp"])

# puedo transformar los datos en distintas cosas
data_dict =  data.to_dict()   # Creo una lista

data_list = data["temp"].to_list() # creo una lista de los datos que contiene "temp"


# METODOS SERIES
data["temp"].mean() # El metodo Mean() saca el promedio de la columna
data["temp"].max() # Devuelve el valor maximo de la serie


# GET DATA IN COLUMNS
# Otra forma de crear serie es directamnte data.condition De esta forma pandas transforma los titulos de las comlumnas
# en atributos que pueden ser llamados.
condition = data["condition"]
condition2 = data.condition
# Estas dos variables son exactamente iguales

# GET DATA IN ROW
# Para obtener todos los datos de una fila tengo que pedirle que busque alguna referencia
# Aca le pido que busque en la columna day un value "Monday" y que me imprima  el row completo
print (data[data.day == "Monday"])

# puedo pedir una informacion particular dentro del row. Por ejemplo si quiero la condition del dia Tuesday
tuesday = (data[data.day == "Tuesday"])

# creada la variable tuesday, puedo usarla como un objeto
print(tuesday.condition)


# CREATE A DATAFRAME
dataframe_dict = {
    "students": ["Amy", "James", "Angelo"],
    "score": [76, 56, 65]
}

data_frame = pandas.DataFrame(dataframe_dict)
#   students  score
# 0      Amy     76
# 1    James     56
# 2   Angelo     65

# Puedo exportar el DF y crear un archivo
# data_frame.to.csv("New_data-csv")