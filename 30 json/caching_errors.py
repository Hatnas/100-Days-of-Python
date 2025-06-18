
#### Caching errors es para evitar el fallo del programa
# Tiene 4 bloques
# Try (donde se pone el codigo a probar)
# Except (Que es lo que tiene que hacer si Try falla)
# Else (lo que pasa si lo que esta en try esta bien)
# Fially (esto tiene que pasar sin importar lo que suceda en los otros bloques)

try:
    file = open("a_file.txt") # esto va  adar error porque la file no exite
    my_dict = {"Name": "Fulano"}
    print (my_dict["mengano"])   # esto va a dar un key error porque no tengo la key "mengano"

except FileNotFoundError:   # Puedo marcar cual es el error que encara el except
    file = open("a_file.txt", "w")  # al abrirlo con "w" lo va a crear
    file.write("Bla Bla Bla")

except KeyError as error_message:
    print (f"{error_message} is not a valid Key")

else:          # esto se va a dar solo si el bloque Try se da entero sin errores
    content = file.read()
    print(content)

finally:
    file.close()
    print("file is closed")



### Ejemplo ###
fruits = ["Apple", "Pear", "Orange"]

def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit Pie")
    else:
        print(f"{fruit} Pie")


make_pie(4)    #esto da un error de index porque solo tiene 3 elementos la lista.

# pero al hacer el try, except, else
# da error en el try y se ejecuta el except