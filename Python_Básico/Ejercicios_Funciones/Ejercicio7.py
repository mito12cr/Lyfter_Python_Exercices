#    Jaime Vanegas Villalobos
#    24/03/2026
#    Python Funciones

# Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma
# [1, 4, 6, 7, 13, 9, 67] → [7, 13, 67]
# Tip 1: Investigue la lógica matemática para averiguar si un número es primo, y conviértala a código. No busque el código, eso no ayudaría.
# Ejercicio 7

def return_list_primo_number(my_list):
    primo_list = []

    for i in my_list:
        if number_primo(i):
            primo_list.append(i)
    return primo_list       


def number_primo(number):
    if number < 2:
        return False
    for i in range (2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

#print (number_primo(7))
#print (number_primo(10))

list_numbers = [1, 4, 6, 7, 13, 9, 67]
result = return_list_primo_number(list_numbers)
print(result)
