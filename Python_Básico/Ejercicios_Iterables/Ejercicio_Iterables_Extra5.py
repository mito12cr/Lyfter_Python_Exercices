#    Jaime Vanegas Villalobos
#    13/03/2026
#    Python Iterables Extra

# Uso .
# Ejercicio 5 Cree un programa que le pida al usuario ingresar 5 palabras. Luego muestre 
# una nueva lista con solo aquellas palabras que tengan más de 4 letras

# Creamos la lista vacía
my_list = []

#pedimos al usuario las palabras estableciendo una lista con un rango de 5 palabras
# y asignamos cada palabra a la variable "word" iniciando en la pocicion 0 de la lista y incrementando en 1 cada vez hasta llegar a 5
# y con el metodo append() agregamos cada palabra al final de la lista.
for i in range(5):
    word = input(f"Digite una palabra {i + 1} : ")
    my_list.append(word)

#Creamos la lista nueva con las palabras que tengan un tamaño mayor a 4 en cada palabra cuando se cumpla la condicion
my_new_list = [num for num in my_list if len(num) > 4]

print(f"\nLista completa: {my_list}")
print(f"Palabras con más de 4 letras: {my_new_list}")