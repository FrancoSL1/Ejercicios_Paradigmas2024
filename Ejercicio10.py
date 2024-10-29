#Ejercicio 10: Operaciones con números de conjuntos.

ListaA = []
ListaB = []
seleccionar = 0
num = 0

print("1. Agregar números al primer conjunto.")
print("2. Agregar números al segundo conjunto.")
print("3. Union de los conjuntos.")
print("4. Intersección de los conjuntos.")
print("5. Diferencia entre los conjunto.")
print("6. Salir.")

while(seleccionar != 6):
 seleccionar = int(input("Opción: "))
 
 if(seleccionar == 1):
  num = int(input("Ingrese un número al primer conjunto: "))
  ListaA.append(num)

 elif(seleccionar == 2):
  num = int(input("Ingrese un número al segundo conjunto: "))
  ListaB.append(num)

 elif(seleccionar == 3):
  num = int(input("¿Quiere ver el prime o el segundo conjunto?"))

  if(num == 1):
   print(ListaA)
  elif(num == 2):
   print(ListaB)
  else:
   print("Esa opción no existe")

 elif(seleccionar == 4): 
  print("Ambos conjuntos:")
  print("Primer conjunto: ",ListaA)
  print("Segundo conjunto: ",ListaB)
 
 elif(seleccionar == 5):
  print(ListaA)

print("Fin del programa")

