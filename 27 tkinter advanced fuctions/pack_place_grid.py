# Para posicionar un widget en la ventana tkinter tiene 3 metodos

# PACK
# pack() junta lo que hay en el widget y lo coloca por default en el centro arriba.
# va a seguir el orden de cada cosas que se fue creando poniendo arriba de todo al primer widget
# y despues a los demas abajo

# en pack se le puede definir el "side"  por ejemplo pack(side= "left".
# de esta forma los coloca en el centro pero a la izquierda


# PLACE
# nos permite definir la posicion con x e y del widget
# al poner sarlaga.place(x= 0, y= 0) lo va a colocar en la esquina superior izquierda


# GRID
# divide la ventana en una grilla. Para posicionar los widget tengo que darles la columna y la fila.
# El valor de la grilla es relativo a los demas widget asi que tengo que ir marcando donde va cada uno
# para que se termine de armar.
