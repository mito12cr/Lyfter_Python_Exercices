#    Jaime Vanegas Villalobos
#    03/03/2026
# Ejercicio 1: 


#Suma de Strings
try:
    name = "jaime"
    last_name = "vanegas"
    
    result = name + last_name
    print(result)
except ValueError:
    print("Error! no puedes sumar dos nombres de esa forma!")


#Suma de String y integer
try:
    name = "jaime"
    number = 50
    result = name + number
    print(result)
except Exception as e:
    print("Error! no puedes sumar un 'String' o caracteres con 'Números' de esa forma!")

#Suma de integer y String 
try:
    number = 50
    name = "jaime"

    result = number + name
    print(result)
except Exception as e:
    print("Error! no puedes sumar 'Números'con un 'String' o caracteres  de esa forma!")

#Suma de list y list 
try:
    list1 = ["jaime, juliana, felipe"]
    list2 = ["marcos, fabiola, hector"]

    result = list1 + list2
    print(result)
except Exception as e:
    print("Error! no puedes sumar dos listas de esa forma!")

#Suma de string y list 
try:
    name = "jaime"
    list1 = ["marcos, fabiola, hector"]

    result = name + list1
    print(result)
except Exception as e:
    print("Error! no puedes sumar un 'String' y una 'Lista' de esa forma!")
    
#Suma de float y int 
try:
    number1 = 50.5
    number2 = 100

    result = number1 + number2
    print(result)
except Exception as e:
    print("Error! no puedes sumar un 'Número Entero' con un 'Números Decimal' de esa forma!")

#Suma de boleano y boleano 
try:
    case1 = True
    case2 = True

    result = case1 + case2
    print(result)
except Exception as e:
    print("Error! no puedes sumar un 2 tipos de 'Booleanos' de esa forma!")

