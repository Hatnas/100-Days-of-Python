### Open read and write files ###

# # Para abrir el archivo. Uso el comando "open" . Lo establezco como un objeto
# file = open("my_file.txt")
#
# # para leer uso el metodo del objeto, que tiene un raturn. y se lo adjudico a una variable
# content =  file.read()
# print(content)
## Para cerrar el File tengo que usar otro metodo.
# file.close()



## Una forma mas practica de hacerlo es: ##
# Usando la key-word With, establezco que la variable file abra el .txt. Sin tener que pensar en cerrarlo.
# Pero si tengo que Indentarlo

with open("my_file.txt") as file:
    content =file.read()
    print(content)

    # Para escribir tengo que llamar al metodo write() del objeto file
    # Para poder escribir tengo que establecer el modo de apertura. Por default esta en "r" (read)
    # tenemos que ponerlo en "w" (write). Esto sobreescribe lo que habia
    # el metodo para agregar es "a"(append)
with open("my_file.txt","a") as file:
    file.write("\nCaballos, muchos caballos")

# Si trato de abrir un file en write mode y este archivo no existe. Este nuevo archivo se va a crear
# with open("new_fie.txt","w") as new_file:
#     new_file.write("This is a new file")

# Para buscar un archivo tengo que poner el path que lleve
# Absolut path (empieza desde C: "\Leo\Programacion\Cursos Python\D24 my new file .txt"
# Relative path. (empieza desde la carpeta donde estamos) "..\..\..\Cursos Python\D24 my new file .txt"
with open("..\..\..\Cursos Python\D24 my new file .txt") as d24:
    print (d24.read())





