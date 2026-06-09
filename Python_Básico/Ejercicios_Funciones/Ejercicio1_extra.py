#    Jaime Vanegas Villalobos
#    25/03/2026
#    Python Funciones

# Cree una función que reciba un texto y un carácter, y retorne cuántas veces aparece ese carácter en el texto
# Ejercicio 1

def return_string(my_text, my_string):
    result = my_text.count(my_string)
    return result

user_text = "programacion"
search_letter = input("Ingrese el carácter que desea buscar: ")
my_result = return_string(user_text, search_letter)

print(f"Se ha encontrado {my_result} veces el caractér en el texto")
