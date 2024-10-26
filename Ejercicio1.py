#Ejercicio1 de grados celsius
#Ingreso de datos
temperatura = float(input("Ingrese la temperatura en grados Celsius: "))

#Categorias de temperatura
if temperatura <= 0:
    print("La temperatura de: ", temperatura,"°C es congelante.")

elif temperatura > 0 and temperatura <= 15:
    print("La temperatura de: ", temperatura,"°C es fria.")

elif temperatura >= 16 and temperatura <= 25:
    print("La temperatura de: ", temperatura,"°C es templada")

else:
    print("La temperatura de: ", temperatura,"°C es calida")
