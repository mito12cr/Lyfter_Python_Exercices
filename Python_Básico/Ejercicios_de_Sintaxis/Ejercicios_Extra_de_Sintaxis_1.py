#    Jaime Vanegas Villalobos
#    04/03/2026
# Ejercicio 1: 

print("Calculo de Descuento y Precio Final de un Producto!!")

product_price = float(input("Ingrese el Precio del Producto a Calcular: "))

if product_price < 100 :
    discount = (product_price * 2) / 100
  
elif product_price >=  100:
    discount = (product_price * 10) /100
final_price = (product_price - discount)       
print(f"El precio Final del producto con su respectivo descuento es de: {final_price}")