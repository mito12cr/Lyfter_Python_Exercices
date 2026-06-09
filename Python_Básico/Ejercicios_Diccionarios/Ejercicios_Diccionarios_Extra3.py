#    Jaime Vanegas Villalobos
#    17/03/2026
#    Python Diccionarios

# Creacion de un diccionario que acumule el total de productos vendidos por categoría.
# Ejercicio 3 extra

products = [
    {"name": "Monitor", "category": "Electrónica", "price": 200},
    {"name": "Teclado", "category": "Electrónica", "price": 50},
    {"name": "Silla"  , "category": "Muebles"    , "price": 120},
    {"name": "Mesa"   , "category": "Muebles"    , "price": 180},
    {"name": "Mouse"  , "category": "Electrónica", "price": 25},
]

total_products_sold = {}

for product in products:
    category = product['category']
    price = product['price']

    total_products_sold[category] = total_products_sold.get(category,0) + price

print(total_products_sold)    

