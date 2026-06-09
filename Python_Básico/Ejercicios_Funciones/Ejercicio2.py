#    Jaime Vanegas Villalobos
#    20/03/2026
#    Python Funciones

# Accediendo a una variable desde otra global.
# Ejercicio 2

var2 = "Global Variable"

#Intente acceder a una variable definida dentro de una función desde afuera

def print_hola_mundo():
    internal_var = "Hola Mundo"


print(internal_var)


#Intente acceder a una variable global desde una función y cambiar su valor.
def change_valor():
    global var2  #utilizamos la palabra reservada 'global' para especificar
    var2 = "Change the global variable"

    
change_valor()
print(var2)    


