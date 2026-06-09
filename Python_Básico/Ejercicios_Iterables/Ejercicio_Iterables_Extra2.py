#    Jaime Vanegas Villalobos
#    13/03/2026
#    Python Iterables Extra

# Uso de una "bandera" para romper y salir del bucle for al cumplir la condicion de que cambie a false cuando encuentre en i un numero 
# menor a "0" siendo por supuesto negativo.
# Ejercicio 2 Cree un programa que verifique si todos los elementos de una lista son positivos

my_list = [3, 6, 0, -2, 4]

positive = True

for i in my_list:
    if i <= 0:  
        positive = False
        break   
if positive:
    print("Todos los números en la lista son positivos")
else:
    print("Hay 1 o mas números negativos en la lista.")       