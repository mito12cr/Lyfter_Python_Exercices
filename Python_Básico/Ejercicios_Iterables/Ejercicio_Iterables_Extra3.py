#    Jaime Vanegas Villalobos
#    13/03/2026
#    Python Iterables Extra

# deducimos que el primer elemento siempre será el menor [0] recorremos el ciclo y asignamos el numero menor segun valla apareciendo
# en la variable smallest_number.
# Ejercicio 3 Cree un programa que muestre el valor más pequeño de una lista sin usar min().

my_list = [9, 4, 7, 1, 5]

smallest_number = my_list[0]

for i in my_list:
    if i < smallest_number: 
        smallest_number = i
print(f"El numero menor de la lista es: {smallest_number}")        