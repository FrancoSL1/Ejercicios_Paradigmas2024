#Ejercicio 2 de descuento de precios
#Ingresar de datos
precio_final = 0
precio_original = float(input("Ingrese el precio del producto: "))

#procesos
if precio_original <= 50:
    print("No hay descuento")

elif precio_original >=51 and precio_original <= 100:
    precio_final = 0.1 * precio_original
    print("El precio final es de: ", precio_final)

else:
    precio_final = 0.2 * precio_original
    print("El precio final es de: ", precio_final)
 