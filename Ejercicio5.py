#Ejercicio 5: Calificación de los estudiantes
#Declarar variables
num_estudiantes = 0
calificacion = 0
promedio = 0

#Ingreso de datos
num_estudiantes = int(input("Ingrese el número de estudiantes: "))

for i in range(num_estudiantes):
 print("Calificación del estudiante N°",i+1)
 calificacion = int(input("Ingrese la calificación:"))
 
 promedio = promedio + calificacion

promedio = promedio / num_estudiantes

#Salida de datos
print("El promedio de los", num_estudiantes," estudiantes es: ", promedio)