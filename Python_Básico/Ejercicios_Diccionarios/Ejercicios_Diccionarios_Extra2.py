#    Jaime Vanegas Villalobos
#    17/03/2026
#    Python Diccionarios

# Creacion de un diccionario agrupando cada empleado por su respectivo departamento.
# Ejercicio 2 extra


employees_by_department = {}
employees = [
    {"name": "Carlos", "email": "carlos@empresa.com", "department": "Ventas"},
    {"name": "Ana", "email": "ana@empresa.com", "department": "TI"},
    {"name": "Luis", "email": "luis@empresa.com", "department": "Ventas"},
    {"name": "Sofía", "email": "sofia@empresa.com", "department": "RRHH"},
]

for employee in employees:
    dept = employee['department']
    
    # Si el departamento no está en el diccionario, creamos una lista vacía
    if dept not in employees_by_department:
        employees_by_department[dept] = []
    
    # Agregamos al empleado a su departamento correspondiente
    employees_by_department[dept].append(employee)
print(employees_by_department) 