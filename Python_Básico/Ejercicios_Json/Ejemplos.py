#    Jaime Vanegas Villalobos
#    22/04/2026
#    Python Archivos Json

# IMPORTAR SIEMPRE LA LIBRERIA Json
import json

# Para convertir de Json a python utilizamos el metodo 'loads()'

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])


# Para convertir de Python a Json utilizamos el metodo dumps()
print("-" *40)

# a Python object (dict):
x = {
 "name": "John",
 "age": 30,
 "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)