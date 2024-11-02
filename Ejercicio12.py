#Ejercicio 12: Registro de calificaciones
ListaNotas = []
ListaNotas2 = []
ListaNombre = []
ListaNombre7 = []
nombre = ""
max = 0
seguir = ""
nota = 0
promedio = 0
cont = 0

num = int(input("Ingrese el número de estudiantes: "))

for i in range(num):
 print("Estudiante ",i+1,":")
 nombre = input("Nombre: ")
 ListaNombre.append(nombre)
 
print("")
print("Calificaciones del primer parcial")
for i in range(num):
 print("Estudiante:",ListaNombre[i])
 nota = int(input("Nota: "))
 ListaNotas.append(nota)

print("")
print("Calificaciones del segundo parcial")
for i in range(num):
 print("Estudiante:",ListaNombre[i])
 nota = int(input("Nota: "))
 ListaNotas2.append(nota)

for i in range(num):
 promedio = (ListaNotas[i]+ListaNotas2[i])/2
 if(promedio > max):
  max = promedio
  nombre = ListaNombre[i]
  
 #Estudiantes que sacaron 7 o mas
 if(promedio >= 7):
  ListaNombre7.append(ListaNombre[i])
  cont = cont + 1
 
print("")
for i in range(num):
 print(ListaNombre[i],", 1°parcial:",ListaNotas[i],",2°parcial:",ListaNotas2[i],"y el promedio total es:",(ListaNotas[i]+ListaNotas2[i])/2)
print("")
print("El estudiante con la nota maxima es:",nombre,"con una nota de",max)
print("")
print("Los estudiantes que aprobaron con más de 7:")
for i in range(cont):
 print(ListaNombre7[i])

