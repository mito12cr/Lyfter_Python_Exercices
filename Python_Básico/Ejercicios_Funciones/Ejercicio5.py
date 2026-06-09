#    Jaime Vanegas Villalobos
#    24/03/2026
#    Python Funciones

# Cree una función que imprima el número de mayúsculas y el número de minúsculas en un string
# Ejercicio 5

def count_upper_and_lower_letters(text):
    upper_letters = 0
    lower_letters = 0

    for charapter in text :
        if charapter.isupper():
            upper_letters += 1
        elif charapter.islower():
            lower_letters += 1
    print(f"There's {upper_letters} upper cases and {lower_letters} lower cases")

count_upper_and_lower_letters("I love Nación Sushi")                    