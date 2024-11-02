#Ejercicio 13: Registro de ventas
ListaVentas = []
ListaTotal = []
cantidad = 0
cont = 0
divi = 0
suma = 0
num = 0
max = 0
promedio = 0

for cont in range(3):
 cont = cont+1
 print("Ingrese cuantas ventas hizo la sucursal ",cont,":")
 cantidad = int(input("multiples ventas: "))
 divi = 0
 promedio = 0

 for i in range(cantidad):
  divi = divi+1
  num = int(input("Venta: "))
  promedio = promedio + num

  #La variable suma es para saber numero total de ventas
  suma = suma + num
 
 ListaTotal.append(promedio)

 #Para calular el promedio de ventas de cada sucursal
 promedio = promedio/divi
 ListaVentas.append(promedio)

print()
print("Total de ventas en todas la sucursales: $",suma)

print()
#Aqui se calcula la sucursal con mayor ventas
for i in range(3):
 if(ListaTotal[i] > max):
  max = ListaTotal[i]
print("Sucursal con mayores ventas acumuladas: Sucursal",i,"con $",max)

print()
for i in range(3):
 print("La sucursal",i+1,"tubo un promedio total de ventas de: $",ListaVentas[i])
