
### LIST COMPREHENSION ###
# Nos permite crear una nueva lista sin utilizar For Loop
# por ejemplo
# Si quiero crear una nueva lista donde cada elemento de numbers sume 1
#
numbers = [1, 2, 3]
# new_list = []
# for n in numbers:
#     add_1 = n + 1
#     new_list.append(add_1)
#
# pero con list comprehension puedo hacerlo en una sola linea
# new_list = [new_item for item in list]
#
# quedaria asi:
new_list = [n+1 for n in numbers]



### CONDITIONAL LIST COMPREHENSION ###

# new_list = [new_item for item in list if test]

# por ejemplo aca le pido que haga lo mismo que antes pero solo si el numero es distitno a 2
new_list_2 = [n+1 for n in numbers if n != 2]

# Aca le pido que los nombres que son mas largo de 4 letras. Los agregue a la lista todos con myusculas.
names =["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
long_cap_names = [name.upper() for name in names if len(name) >4]