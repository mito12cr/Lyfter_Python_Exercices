#    Jaime Vanegas Villalobos
#    24/03/2026
#    Python Funciones

# Cree una función que acepte un string con palabras separadas por un guion y retorne un string igual pero ordenado alfabéticamente.
# Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.
# Ejercicio 6

def alphabetic_order(text):
    my_list = text.split("-")  # utilizamos la funcion split() para dividir el texto y guardarlo en una lista utilizando el "-" como separador

    my_list.sort()             # ordenamos la lista alfabeticamente

    return "-".join(my_list)   # con la funcion join() se hace lo contrario al split() para unir los elementos de la lista y formar un solo string insertando el "-" como conector de cada elemento

result = alphabetic_order('python-variable-funcion-computadora-monitor')
print(result)