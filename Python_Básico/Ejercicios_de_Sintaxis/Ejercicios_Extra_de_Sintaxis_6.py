#    Jaime Vanegas Villalobos
#    04/03/2026
# Ejercicio 6: 

print("Algoritmo de Tablas de Multiplicar !!")

number = int(input("Digite el Número de Multiplo que desea conocer "))

if 1 <= number <= 10 :
    print(f"n\Esta es la tabla de multiplicar del numero {number} :")
    for i in range(1,13):
        result = number * i
        print(f"{number} x {i} = {result}")
else :
    print("El número digitado debe estar en un rango entre el 1 y 10")        