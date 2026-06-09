#    Jaime Vanegas Villalobos
#    13/03/2026
#    Python Iterables

# Uso de la Asignacion Multiple, para intercambiar valores
# Ejercicio 3 Cree un programa que intercambie el primer y ultimo elemento de una lista. Debe funcionar con listas de cualquier tamaño.

my_list = [4, 3, 6, 1, 7]

my_list[0], my_list[-1] = my_list[-1],my_list[0]
print(my_list)