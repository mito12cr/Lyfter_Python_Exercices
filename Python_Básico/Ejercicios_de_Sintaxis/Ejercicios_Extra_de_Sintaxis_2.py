#    Jaime Vanegas Villalobos
#    04/03/2026
# Ejercicio 2: 

print("Calculo de Tiempo en segundos!!")

time_seconds = int(input("Digite el tiempo a calcular en segudos: "))

if time_seconds < 600 :
    remaining_seconds = 600 - time_seconds
    print(f"El tiempo restante equivalentes en segundos para llegar a 10 minutos es :  {remaining_seconds} segundos!!")
elif time_seconds > 600:
    print(f"El tiempo Digitado es Mayor")
elif time_seconds == 600 :
          print(f"El tiempo Digitado es Igual al equivalente a 10 minutos en segundos")