
### Dia 1 Variables ###

print ("Bienvenido al generador de nombres para bandas")
city = input("Cual es el nombre de la ciudad donde cresiste\n")
mascota = input("Como se llama tu mascota?\n")
print ("El nombre de tu banda podria ser ", city, mascota)


### Dia 2 Tip Calculator ###

cuenta = int(input ("De cuanto es la cuenta? "))
porcentaje = int(input ("Cual es el pocentaje de la propina? "))
personas = int(input ("Cuantos son para dividir? "))

propina = cuenta * 100 / porcentaje
propina_por_cliente = porcentaje / personas

print ("Serian ", propina_por_cliente, "cada uno")


