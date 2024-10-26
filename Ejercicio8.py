#Ejercicio 8: Control de Stock
inventario = 0
transaccion = 0
total = 0
validar = True
validar_dos = True
validar_tres = True
validar_cuatro = True
producto = " "
venta_compra = " "
seguir = " "

print("***************************************")
print("*Bienvenido al inventario de la tienda*")
print("***************************************")

while validar_tres:
    producto = input("Ingrese el nombre del producto: ")
    total = total + 1
    
    #Ingresar venta o compra
    while validar:
     venta_compra = input("¿Es una venta o una compra? ")

     if venta_compra == "venta" or venta_compra == "compra":
        validar = False
     else:
        print("\n Error solamente se puede poner venta o compra \n")

    validar = True
    
    #inventario o transacción
    if venta_compra == "compra":
       inventario = inventario + 1
       print("\n La compra se ha realizado con exito \n")

    elif venta_compra == "venta":
       while validar_cuatro:
          cantidad = input("Antes de hacer la transacción ¿hay suficiente cantidad en el stock? ¿si o no? ")
          
          if cantidad == "si" or cantidad == "no":
             validar_cuatro = False
          else:
             print("\n Error solo se puede poner si o no \n")

       if cantidad == "si":
          print("\n La transacción se ha realizado con exito \n")
          transaccion = transaccion + 1
       elif cantidad == "no":
          print("\n No hay sufiente en el stock \n")

    validar_cuatro = True
    
    #Continuar si o no
    while validar_dos:    
       seguir = input("desea continuar? ¿si o no? ")

       if seguir == "si" or seguir == "no":
          validar_dos = False
       else: 
          print("\n Error solo se puede poner si o no \n")

    validar_dos = True
    
    if seguir == "si":
       validar_tres = True
    elif seguir == "no":
       validar_tres = False
       
#Salida de datos
print("Cantidad de producto total es: ", total)
print("El número total de inventario es: ", inventario)
print("El número total de transacciones realizadas: ", transaccion)
print("Fin del programa")
    