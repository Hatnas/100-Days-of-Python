
############DEBUGGING#####################

# # Describe Problem
# def my_function():
#   for i in range(1, 20):
#     if i == 20:
#       print("You got it")
# my_function()
#  # Nunca i == 20 porque 20 queda excluido del range 
#  # solucion range(1, 21)

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num =  randint(1, 6)
# print(dice_imgs[dice_num])
    # # Al poner randit 1, 6 estamos omitiendo las posiciones 0 y agregando una posicion inexistente de la lista
    # # si dice_num = 6 va a dar error porque la lista solo tiene hasta poscion 5
    # # para reproducir el error dice_num = 6
    # # para corregirlo ranint(0, 5)

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")
#     # 1994 queda excluido de ambas condiciones por lo que no da ningun resultado
#     # hay que incluirlo dentro de alguna de las dos opciones <= 1994 o >= 1994

# # Fix the Errors
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")
#     # Tiene varios errores. "age" tiene que ser in int para poder ser comparado 
#     # age puede ser >= 18
#     # el print esta mal indentad
#     # Seria:
#  # age = int(input("How old are you?"))
#  # if age >= 18:
#  #     print("You can drive at age {age}.")


# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)
# # esta mal el == en word_per_page tendria que ser =
# # podria poner un print despues de establecer cada variable


# #Use a Debugger
# ######  https://pythontutor.com/render.html#mode=display ######
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   print(b_list)
#   # b_list.append(new_item) esta mal indentado quedando afuera del loop for

# mutate([1,2,3,5,8,13])