#    Jaime Vanegas Villalobos
#    17/03/2026
#    Python Diccionarios

# Creacion de un diccionario nuevo que guarde el total de ventas de cada UPC.
# Ejercicio 1 extra


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

#Creamos el nuevo diccionario donde guardará el total de ventas por cada "UPC"
result = {}
for sale in sales :                                  # Iteramos o recorremos todo el diccionario
    for item in sale ['items']:                      # Iteramos en cada item de cada venta
        upc = item['upc']                            # Asignamos cada upc de cada item de cada venta a la variable 'upc'
        price = item['unit_price']                   # Realizamos el mismo procedimiento con el precio de cada  item
        result[upc] = result.get(upc,0) + price         
print(result)        