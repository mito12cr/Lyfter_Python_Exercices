#    Jaime Vanegas Villalobos
#    16/03/2026
#    Python Diccionarios

# Creacion de un diccionario a patir de 2 listas.
# Ejercicio 2 
# Se utiliza la funcion zip() para emparejar los elementos de ambas litas, junto con el 
# constructor dict() convirtiendo cada par de los elementos de las dos listas en su respectivo "key" y "Value" respectivos.

list_a = ["first_name", "last_name", "role"]
list_b = ["Alek", "Castillo" ,"Software Engineer"]

new_users = dict(zip(list_a,list_b))
print(new_users)