#    Jaime Vanegas Villalobos
#    13/03/2026
#    Python Iterables

# Uso de la funcion Max() para obtener el numero mas alto en los ingresados.
# Ejercicio 5 Cree un programa que le pida al usuario 10 números, y al final le muestre todos los números
#  que ingresó, seguido del numero ingresado más alto.

my_numbers = []

for i in range(10):
    num1 = int(input(f" Ingrese 10 Números al asar {i + 1}: "))
    my_numbers.append(num1)

print("\nEstos son los 10 Numeros ingresados: ", my_numbers)
print("El Número Mayor de los 10 es el: ", max(my_numbers))