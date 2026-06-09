#    Jaime Vanegas Villalobos
#    13/03/2026
#    Python Iterables

# Uso del Método Range()
# Ejercicio 2. Cree un programa que itere e imprima un string letra por letra de derecha a izquierda.

# [inicio:fin:paso]

my_string = "Pizza con piña"

for i in range(len(my_string) - 1, -1, -1):
    print(my_string[i])
