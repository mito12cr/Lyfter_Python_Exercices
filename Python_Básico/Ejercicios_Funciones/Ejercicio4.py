#    Jaime Vanegas Villalobos
#    24/03/2026
#    Python Funciones

# Cree una función que le dé la vuelta a un string y lo retorne.
# Ejercicio 4


def rotate_string(var_string):
    return var_string[::-1]    #utilizando esta expresion '[::-1] decimos que recorra el texto desde el final hasta el principio con un paso de -1 esto hará que valla de derecha a izquierda.
                                

result = rotate_string("hola mundo")
print(result)