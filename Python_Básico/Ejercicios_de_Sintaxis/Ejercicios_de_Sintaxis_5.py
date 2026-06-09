#    Jaime Vanegas Villalobos
#    03/03/2026
# Ejercicio 5: 

grade_counter = 1
number_of_grades_approved = 0
number_of_failed_grades = 0
average_of_passing_grades = 0
average_of_failing_grades = 0
average_of_total_grades = 0

print("Bienvenido al Càlculo de Notas!!!")

total_of_grades = int(input("Digite la cantidad de notas del estudiante: "))

while grade_counter <= total_of_grades :
    try: 
         print(f"Ingrese la nota numero {grade_counter}")
         current_note = float(input())

         if current_note < 70 :
             number_of_failed_grades += 1
             average_of_failing_grades += current_note
         else:
             number_of_grades_approved += 1
             average_of_passing_grades += current_note    

         average_of_total_grades += (current_note/total_of_grades)
         grade_counter += 1   

    except ValueError as e:
        print("Debes digitar un número valido del 1 al 10!!")   
   
if number_of_failed_grades > 0 :
    average_of_failing_grades /= number_of_failed_grades

if number_of_grades_approved > 0 :
   average_of_passing_grades /= number_of_grades_approved 
print(f"\nEl total de notas mayor a 70 del estudiante es de:      {number_of_grades_approved}")       
print(f"\nEl promedio de notas del estudiante aprobadas es de:    {average_of_passing_grades}")  
print(f"\nEl total de notas menor a 70 del estudiante es de:      {number_of_failed_grades}")  
print(f"\nEl promedio de notas del estudiante desaprobadas es de: {average_of_failing_grades}")  
print(f"\nEl promedio total de notas del estudiante es de:        {average_of_total_grades}")  