
## ADVANCED ARGUMENTS ##
# Algunas funciones pueden tener argumentos preestablecidos. Los cuales son opcionales de ser modificados
# o no. Por ejemplo "font".
# Otros argumentos son "requiered". Es decir que si o si los tengo que poner para que la funcion corra
# Los esta forma de plantear argumentos tambien se usan al DEFINIR UNA CLASE


# Unlimeted Positional Arguments
# Para que una fucion acepte una cantidad ilimitada de argumentos tengo que poner *args.
# En realidad lo unico importante es el * lo mismo da si le pongo *n

def foo(*args):
    for n in args:
        print (n)


# Unlimetd Key Word Arguments (v007)
# Para poder referirnos a argumentos por su key, es parecido a lo anterior.. solo que con dos ** y se usa kwargs
# Esto va a crear un dict y yo puedo axeder tanto a las key como a los value del mismo

def calculate(**kwargs):
    for key,value in kwargs.items():
        print (key)
        print (value)



calculate(add= 3, multiply= 5)
