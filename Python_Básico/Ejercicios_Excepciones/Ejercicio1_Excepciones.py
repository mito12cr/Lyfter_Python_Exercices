#    Jaime Vanegas Villalobos
#    30/03/2026
#    Python Excepciones

# Cree una calculadora por linea de comando. Esta debe de tener un número actual, y un menú para decidir qué operación hacer con otro número:
#1. Suma
#2. Resta
#3. Multiplicación
#4. División
#5. Borrar resultado
# Al seleccionar una opción, el usuario debe ingresar el nuevo número a sumar, restar, multiplicar, o dividir por el actual. El resultado debe pasar a ser el nuevo numero actual.
# Debe de mostrar mensajes de error si el usuario selecciona una opción invalida, o si ingresa un número invalido a la hora de hacer la operación.
# Ejercicio 1

def addition(num1,num2):
    return num1 + num2


def subtraction(num1,num2):
    return num1 - num2


def multiplication(num1,num2):
    return num1 * num2


def division(num1, num2):
    if num2 == 0:
        print("Error, no se puede dividir por cero (0)")
        return num1
    else:
        return num1 / num2    


def calculadora():
    current_number = 0.0

    while True:
        print(f"\n El numero actual es: {current_number}")
        print("1. Para SUMAR")
        print("2. Para RESTAR")
        print("3. Para MULTIPLICAR")
        print("4. Para DIVIDIR")
        print("5. Para BORRAR DATOS")
        print("6. Para SALIR")

        opcion = input("Seleccione una operacion del 1 al 6: ")

        if opcion == "5":
            current_number = 0.0
            print("Se ha Borrado el resultado")
            continue  

        if opcion == "6":
            print("Has Salido del Programa")
            break          

        if opcion not in ['1','2','3','4']:
            print("Error: La opcion no es válida por favor ingresar un número dentro del rango!!")
            continue

        try:
            entrance = input("Digite el siguiente número de la ecuación: ")
            new_current_number = float(entrance)
            break
        except ValueError as e: 
            print(f"ERROR: Debe digitar un número válido, {e}")

            match opcion:
                case "1":
                    current_number = addition(current_number , new_current_number)
                case "2":
                    current_number = subtraction(current_number,new_current_number)
                case "3": 
                    current_number = multiplication(current_number,new_current_number)
                case "4":
                    current_number = division (current_number,new_current_number)                   
        

calculadora()            
