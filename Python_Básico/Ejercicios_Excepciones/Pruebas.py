


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
            new_current_number = float(input("Digite el siguiente número de la ecuación: "))

            match opcion:
                case "1":
                    current_number += new_current_number
                case "2":
                    current_number -= new_current_number
                case "3": 
                    current_number *= new_current_number
                case "4":
                    if new_current_number == 0:
                        print("ERROR: No se puede dividir por cero")
                    else:
                        current_number /= new_current_number
        except ValueError as e: 
            print("ERROR: Debe digitar un número válido {e}")

calculadora()      


def convertir_a_entero(lista):
    enteros = []
    
    for item in lista:
        try:
            # Intentamos la conversión
            numero = int(item)
            enteros.append(numero)
        except ValueError:
            # Si falla, imprimimos el mensaje solicitado y el bucle sigue
            print(f"No se pudo convertir el elemento: <{item}>")
            
    return enteros

# Prueba de la función
datos = ["10", "abc", "25", "3.14", "100"]
resultado = convertir_a_entero(datos)

print(f"\nLista de resultados exitosos: {resultado}")



def print_names():
    name = input("Escriba su nombre aquí: ").strip()
     
    # Validamos que el nombre no contenga números
    if any(char.isdigit() for char in name):
        print("Error: El nombre no puede contener números.")
        return # Salimos de la función si hay error
    
    if not name:
        print("Error: El nombre no puede estar vacío.")
        return

    age_input = input("Digite su edad: ")
    
    try:
        # Intentamos convertir directamente
        age = int(age_input)
        
        if age < 0:
            print("Error: La edad no puede ser negativa.")
            return

        print(f"Hola {name}, su edad es {age}!!")  

    except ValueError:     
        print("Error: Debe digitar un número entero válido para la edad.")

print_names()
6