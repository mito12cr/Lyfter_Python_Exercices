#    Jaime Vanegas Villalobos
#    31/03/2026
#    Python Excepciones

# Cree una función convertir_a_entero(lista) que:
# Reciba una lista de strings
# Intente convertir cada elemento a entero usando int()
# Use try-except para atrapar los errores ValueError
# Si algún elemento no puede convertirse, mostrar "No se pudo convertir el elemento: <valor>" y continuar con los demás

def convertir_a_entero(my_list):

    print("Resultado:")
    new_list = []

    for i in my_list:
        try:
             number = int(i)
             print(f"{i} convertido a: {number}")
             new_list.append(number)       

        except ValueError:
          print(f"No se puede convertir el elemento: {i} a un número")

   
    return new_list
  
my_list = ['4','hola','10','5.2']
result = convertir_a_entero(my_list)  


