#    Jaime Vanegas Villalobos
#    03/03/2026
# Ejercicio 4: 

print("Bienvenido al juego del number mayor!!!")
print("A continuacion digite 3 números de su agrado para conocer cual de los 3 es el Mayor")

number1 = int(input("Digite el Primer Número: "))
number2 = int(input("Digite el Segundo Número: "))
number3 = int(input("Digite el Tercer Número: "))

if number1 > number2 and number1 > number3 :
    print("El Número mayor es: " + f'{number1}')
elif number2 > number1 and number2 > number3 :
    print("El Número mayor es: " + f'{number2}')
else :
    print("El Número mayor es: " + f'{number3}')