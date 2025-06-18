### Classes ###

# Una clase tiene "Atributos" Que son variables que las caracterizan
# y, por otro lado tiene "Metodos" Que son funciones que determinan que hace

#La data de PrettyTable esta en https://pypi.org/project/prettytable/
# Para crear un objeto que sea de una clase tenemos que primero establecer la clase
#eso lo hacemos importando la clase "PrittyTable"

from prettytable import PrettyTable

#Ya teniendo la clase creo una "variable" que la vinculo con la clase
table = PrettyTable()
print (table)

table.add_column("Pokemon Name",["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align = "l"
print (table)
