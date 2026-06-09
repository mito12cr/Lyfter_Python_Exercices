#    Jaime Vanegas Villalobos
#    04/03/2026
# Ejercicio 4: 

print("Algoritmo de validacion con el numero 30!!")

first_number  = int(input("Digite el primer número: "))
second_number = int(input("Digite el segundo número: "))
third_number  = int(input("Digite el tercer número: "))

numbers = [first_number,second_number,third_number]

if 30 in numbers or sum(numbers) == 30:
    print ("Correcto!!")
else : 
    print ("Incorrecto!!")
