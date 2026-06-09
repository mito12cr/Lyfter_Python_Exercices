#    Jaime Vanegas Villalobos
#    03/03/2026
# Ejercicio 2: 

name = input("Ingrese su name: ")
last_name = input("Ingrese su last_name: ")
age = int(input("Ingrese su age: "))

if age <= 6 :
    print("Eres un niño")

elif  age > 6 and age <= 12 :
    print("Eres un preadolecente! ")

elif  age > 12 and age <= 18 :
    print("Eres un Adolecente! ")

elif  age > 18 and age <= 30 :
    print("Eres un Adulto Joven! ")

elif  age > 30 and age <= 65 :
    print("Eres un Adulto! ")

else:
    print("Eres un Adulto Mayor! ")


