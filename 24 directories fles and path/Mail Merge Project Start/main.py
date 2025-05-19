
### Creacion de varias cartas cambiando el destinatario!!!!


#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("./Input/Names/invited_names.txt","r") as names_file:
    names = names_file.readlines()     # Devuelve una List de todas las lineas del texto


# Remplazar [name] en el txt starting_letter, NO ME RECONOCE LA FUNCION REPLACE
with open("./Input/Letters/starting_letter.txt") as starting_file:
    letter_content = starting_file.read()    # Devuelve un str de el archivo completo
    for name in names:
        strip_name =name.strip()     # elimino lo que esta entre parentesis , es decir \n
        new_letter = letter_content.replace("[name]", strip_name )  # replace se usa con una str para remplazar
        with open (f"./Output/ReadyToSend/letter_for_{strip_name}.txt", "w") as completed_letter:  # Crea un archivo .txt en destino
            completed_letter.write(new_letter)  # Escribo sobre lo que habia la nueva carta





