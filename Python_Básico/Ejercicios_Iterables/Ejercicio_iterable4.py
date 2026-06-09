#    Jaime Vanegas Villalobos
#    13/03/2026
#    Python Iterables

# Uso de comprension de listas(list comprehension)
# Ejercicio 4 Cree un programa que elimine todos los números impares de una lista.

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

my_list = [num1 for num1 in my_list if num1 % 2 ==0]

print(my_list)

#Investigando se dice que la mejor forma es crear una lista nueva a partir de la 1era, con la condicion de que los numeros que se 
# impriman(en este caso PARES) sean dividibles entre 2 para ser mostrados en la nueva lista.