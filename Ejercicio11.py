#Ejercicio 11: Análisis de números
ListaA = []
num = 0
max = 0
min = 999999
suma = 0
cont = 0
cont2 = 0
seleccionar = 0

print("1. Agregar un número a la lista")
print("2. Mostrar el número mayor y menor de la lista")
print("3. Calcular la suma y el promedio")
print("4. Contar cuantos numeros son pares")
print("5. Salir del programa")

while(seleccionar != 5):
 seleccionar = int(input("Opción: "))
 
 if(seleccionar == 1):
  num = int(input("Ingrese un número en la lista: "))
  ListaA.append(num)
  cont = cont + 1

 elif(seleccionar == 2):
  for i in range(cont):
   if(ListaA[i] > max):
    max = ListaA[i]
   if(ListaA[i] < min):
    min = ListaA[i]
  print("El numero más grande de la lista es: ", max)
  print("El número más pequeño de la lista es: ", min)
 
 elif(seleccionar == 3):
  for i in range(cont):
   suma = suma + ListaA[i]
  print("La suma total es: ", suma)
  print("El promedio total es: ", (suma/cont))

 elif(seleccionar == 4):
  for i in range(cont):
   suma = ListaA[i] % 2
   if(suma == 0):
    cont2 = cont2 + 1
  print("Cantidad de números pares: ", cont2)

print("Fin del programa")