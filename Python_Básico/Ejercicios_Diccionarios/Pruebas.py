new_dictionary = {
    "key_1": "valor1",
    "key_2": "valor2",
    "key_3": "valor3",
    "key_4": "valor4",
    "key_5": "valor5",    
}

#metodo items()
for key,value in new_dictionary.items():
    print(key)
    print(value)

#metodo keys()    
for key in new_dictionary.keys():
    print(key)

#metodo keys()    
for value in new_dictionary.values():
    print(value)


list_a = ['first_name', 'last_name', 'role']
list_b = ['Alek', 'Castillo', 'Software Engineer']

# Se combinan las listas y se transforman en diccionario
resultado = dict(zip(list_a, list_b))

# print(resultado)


sales = [
	{
		'date': '27/02/23',
		'customer_email': 'joe@gmail.com',
		'items': [
			{
				'name': 'Lava Lamp',
				'upc': 'ITEM-453',
				'unit_price': 65.76,
			},
			{
				'name': 'Iron',
				'upc': 'ITEM-324',
				'unit_price': 32.45,
			},
			{
				'name': 'Basketball',
				'upc': 'ITEM-432',
				'unit_price': 12.54,
			},
		],
	},
	{
		'date': '27/02/23',
		'customer_email': 'david@gmail.com',
		'items': [
			{
				'name': 'Lava Lamp',
				'upc': 'ITEM-453',
				'unit_price': 65.76,
			},
			{
				'name': 'Key Holder',
				'upc': 'ITEM-23',
				'unit_price': 5.42,
			},
		],
	},
	{
		'date': '26/02/23',
		'customer_email': 'amanda@gmail.com',
		'items': [
			{
				'name': 'Key Holder',
				'upc': 'ITEM-23',
				'unit_price': 3.42,
			},
			{
				'name': 'Basketball',
				'upc': 'ITEM-432',
				'unit_price': 17.54,
			},
		],
	},
]

result = {}
for sale in sales:
    for item in sale['items']:
        upc = item['upc']
        price = item['unit_price']
        # Sumamos al valor existente o inicializamos en 0 si es un UPC nuevo
        result[upc] = result.get(upc, 0) + price
print(result)

print(" ")

result = {}


employees = [
    {"name": "Carlos", "email": "carlos@empresa.com", "department": "Ventas"},
    {"name": "Ana", "email": "ana@empresa.com", "department": "TI"},
    {"name": "Luis", "email": "luis@empresa.com", "department": "Ventas"},
    {"name": "Sofía", "email": "sofia@empresa.com", "department": "RRHH"},
]

for employee in employees:
    dept = employee['department']
    
    # Si el departamento no está en el diccionario, creamos una lista vacía
    if dept not in result:
        result[dept] = []
    
    # Agregamos al empleado a su departamento correspondiente
    result[dept].append(employee)
print(result)

print("   ")


products = [
    {"name": "Monitor", "category": "Electrónica", "price": 200},
    {"name": "Teclado", "category": "Electrónica", "price": 50},
    {"name": "Silla", "category": "Muebles", "price": 120},
    {"name": "Mesa", "category": "Muebles", "price": 180},
    {"name": "Mouse", "category": "Electrónica", "price": 25},
]

result = {}

for product in products:
    cat = product['category']
    price = product['price']
    
    # Si la categoría no existe, empezamos en 0 y sumamos el precio
    # Si ya existe, le sumamos el precio al total que ya teníamos
    result[cat] = result.get(cat, 0) + price
print(result)