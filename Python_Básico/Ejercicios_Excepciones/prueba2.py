def calculadora():
    actual = 0.0
    
    while True:
        print(f"\n--- Número actual: {actual} ---")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Borrar resultado (Reset)")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "6":
            print("¡Adiós!")
            break
        
        if opcion == "5":
            actual = 0.0
            print("Resultado borrado.")
            continue

        if opcion not in ["1", "2", "3", "4"]:
            print("Error: Opción no válida. Intente de nuevo.")
            continue

        try:
            nuevo_numero = float(input("Ingrese el número: "))
            
            match opcion:
                case "1":
                    actual += nuevo_numero
                case "2":
                    actual -= nuevo_numero
                case "3":
                    actual *= nuevo_numero
                case "4":
                    if nuevo_numero == 0:
                        print("Error: No se puede dividir por cero.")
                    else:
                        actual /= nuevo_numero
        except ValueError:
            print("Error: Debe ingresar un número válido.")

if __name__ == "__main__":
    calculadora()




#---------------------------------------------------------



def calculadora():
    try:
        print("Bienvenido al programa de calculadora, por favor siga las instrucciones y lea cuidadosamente cada una de ellas")
        print("Elija una opcion a realizar en la calculadora")
        opcion = input("Digite alguna opcion a realizar: 1 para SUMAR, 2 para Restar, 3 para MULTIPLICACION, 4 Para DIVISIÓN Y 5 Para BORRAR y REINICIAR")
        
        if opcion == 1:
            suma()
        elif opcion == 2:
            resta()
        elif opcion == 3:
            multiplicacion()
        elif opcion == 4:
            division()    

            

    except TypeError as e:
        print(f"Error [TypeError] Error al sumar: {e} ") 

calculadora()   

def suma(val1,val2):
   valor1 = input("Digite el primer valor para SUMAR: ")
   valor2 = input("Digite el segundo valor para SUMAR: ")
   result = valor1 + valor2
   print("El total de la suma es de: {result}")
   return result


def resta(val1,val2):
   valor1 = input("Digite el primer valor para Restar: ")
   valor2 = input("Digite el segundo valor para Restar: ")
   result = valor1 - valor2
   print("El total de la resta es de: {result}")
   return result


def multiplicacion(val1,val2):
   valor1 = input("Digite el primer valor para Multiplicar: ")
   valor2 = input("Digite el segundo valor para Multiplicar: ")
   result = valor1 * valor2
   print("El total de la Multiplicacion es de: {result}")
   return result


def division(val1,val2):
   valor1 = input("Digite el primer valor para Dividir: ")
   valor2 = input("Digite el segundo valor para Dividir: ")
   result = valor1 / valor2
   print("El total de la Division es de: {result}")
   return result