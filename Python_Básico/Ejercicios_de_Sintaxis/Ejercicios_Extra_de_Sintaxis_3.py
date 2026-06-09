#    Jaime Vanegas Villalobos
#    04/03/2026
# Ejercicio 3: 

count = 1
sum_total_numbers = 0

print("Suma de numeros en 1 hasta el número ingresado!!")

requested_number = int(input("Digite el Número Solicitado: "))

while count <= requested_number :
    sum_total_numbers = sum_total_numbers + count
    count = count +1
print(f"La suma de cada número ingresado hasta el número inicial es de : {sum_total_numbers}")    
