#    Jaime Vanegas Villalobos
#    13/03/2026
#    Python Iterables Extra

# Uso .
# Ejercicio 4 Cree un programa que reciba una lista de números y 
# calcule el promedio de los valores, luego cree una nueva lista con solo los valores mayores al promedio

my_list = [10, 20, 30, 40, 50]

#calculamos el promedio con la suma de numeros totales de los elementos de la lista = 150
# y lo dividimos con el total de elementos de la lista que serian 5 en totales dando 30 como resultado ese es el promedio.
average = sum(my_list) / len(my_list)

#Creamos una nueva lista con los numeros mayores al promedio cumpliendo la condicion que sean mayor al promedio
higher_than_average = [num for num in my_list if num > average]

print(f"El promedio de los numeros de la lista es de: {average}")
print(f"Los valores mayores al promedio son: {higher_than_average}")