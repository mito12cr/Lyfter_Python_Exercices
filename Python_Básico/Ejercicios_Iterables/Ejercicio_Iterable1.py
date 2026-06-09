#    Jaime Vanegas Villalobos
#    05/03/2026
#    Python Iterables

# Uso del Método Zip()
# Ejercicio 1 Cree un programa que itere e imprima los valores de dos listas del mismo tamaño al mismo tiempo.

first_list = ['Hay', 'en', 'que', 'iteracion', 'indices', 'muy']

second_list = ['casos', 'los', 'la', 'por', 'es', 'util']

for i in range(len(first_list)):
    print(first_list[i],second_list[i])

#for index1,index2 in zip(first_list,second_list):
#    print(index1,index2)


print("   ")

    #Prueba de 3 listas
first_list = ['Hay', 'en','la',  'indices', 'mejor','aspectos']

second_list = ['casos', 'los','iteracion', 'es', 'por', 'en', 'muy']

third_list = ['concretos', 'que', 'por', 'la', 'ciertos', 'concreto']

for i in range(len(first_list)):
    print(first_list[i],second_list[i],third_list[i])

#for index1,index2,index3 in zip(first_list,second_list,third_list):
#    print(index1,index2,index3)