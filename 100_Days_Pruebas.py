var_a = "Hola"

def modificacion():
    global var_a
    if input("Chau?").lower() == "si":
        var_a = "Chau"

modificacion()
print (var_a)