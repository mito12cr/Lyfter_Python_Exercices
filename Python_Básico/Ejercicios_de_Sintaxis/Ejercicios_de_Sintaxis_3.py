#    Jaime Vanegas Villalobos
#    03/03/2026
# Ejercicio 3: 
import random

secret_number = random.randint(1,10)
chance = 0

print("Juego al Número Secreto!!")

while chance != secret_number :
    try :
        chance = int(input("Digita un número del 1 al 10 Máximo!!"))

        if chance < secret_number :
            print("Tu número es más bajo que el número Secreto")
        elif chance > secret_number :
            print("Tu número es Mayor al Número Secreto!!")
        else :
            print("Has Acertado al Número Secreto Excelente!!")

    except ValueError:
        print("Debes digitar un número valido del 1 al 10!!")
print("Gracias por participar!!") 