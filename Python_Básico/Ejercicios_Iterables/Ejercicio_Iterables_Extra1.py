#    Jaime Vanegas Villalobos
#    13/03/2026
#    Python Iterables Extra

# Uso de la funcion Count().
# Ejercicio 1 Cree un programa que cuente cuántas veces aparece un número específico
#  en una lista. Pida al usuario una lista de números y otro número a buscar

my_list = [4, 2, 7, 2, 8, 2, 1]
number_to_search = 2

repeated_times = my_list.count(number_to_search)

print(f"\nEl Número a buscar es: {number_to_search} y aparece un total de: {repeated_times} veces")