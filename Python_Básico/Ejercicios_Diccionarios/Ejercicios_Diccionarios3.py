#    Jaime Vanegas Villalobos
#    16/03/2026
#    Python Diccionarios

# Eliminando "Keys" de un diccionario a partir de una lista.
# Ejercicio 3 
# 
# 

list_of_keys = ["access_level", "age"]  
employee = {"name": "john", "email": "john@ecorp.com", "access_level": 5, "age": 28}

for key in list_of_keys:
    employee.pop(key,None)

print(employee)

# Investigando un poco más para eliminar "Keys" de un diccionario; encontré que se puede utilizar un diccionario por conprension
# queriendo decir que se crea un nuevo diccionario que solo incluya los "keys" que no estan en la lista de la siguiente manera

list_of_keys = ['access_level', 'phone_number']
employee = {'name': 'John', 'email': 'john@ecorp.com', 'access_level': 5, 'age': 28,'phone_number': 894465177,'country':"USA"}

# Creamos un nuevo diccionario filtrando las llaves
resultado = {i: v for i, v in employee.items() if i not in list_of_keys}

print(resultado)
