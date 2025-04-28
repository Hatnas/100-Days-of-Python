
### Cesar Cipher ###

## 001  Functions and inputs

# def greet_with_name(name):    # "name" es el "PARAMETRO" y "Leo" seria el "ARGUMENTO"
#     print (f"Hello! {name}")
#     print (f"How do you do {name}?")

# greet_with_name("Leo")


## Functions with more than one input


def greet_with(name, location):
    print (f"Hello {name}")
    print (f"How is like in {location}")

# Psitional Argument
greet_with("Leo", "CABA")         # esto es Positional argument. No diferencia el tipo de value sino la posicion en la "cadena"

# Keyword Argument
greet_with(location="CABA", name="Leo")         # esto es Keyword argument y vinculo un argumento a su Parametro. Por lo que no dependo del orden


# 004 
import math
def paint_calc(height, widht, cover):
    number_of_can = math.ceil((height * widht) / cover)  # la funcion .ceil redondea para arriba. Esta dentro del modulo Math
    print (f"you´ll need {number_of_can} cans of paint")

test_h = int(input())
test_w = int(input())
coverage = 5

paint_calc(height = test_h, widht = test_w, cover = 5)


# 005 Prime number checker
def prime_checker (number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
         is_prime = False
         
    if number == 1:
       is_prime = False

    if is_prime == True:
        print(f"{number}, is a prime number")
    else:
        print(f"{number}, is not a prime number")

n = int(input())
prime_checker(number = n)



                  ### 009 Cesar Cipher ###

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def cesar(start_text, shift_amount, cipher_direction):
    if shift > 26:
        shift_amount = shift % 26

    final_text = ""
    for letter in start_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            if cipher_direction == "encode":
                new_position = position + shift_amount
            elif cipher_direction== "decode":
                new_position = position - shift_amount
            new_letter = alphabet[new_position]
        else:
            new_letter = letter
        final_text += new_letter
    print (f"The {cipher_direction}d word is {final_text}")


again =True
while again == True:
    print (logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    cesar(start_text= text, shift_amount= shift, cipher_direction= direction)
    answer = input("Want to go again?\n")
    if answer == "no":
        print ("We are done!")
        again = False
    elif answer == "yes":
        again = True
    else:
        answer = input("Want to go again?\n")