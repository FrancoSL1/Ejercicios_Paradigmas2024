#Ejercicio 4: categoría de velocidades

kilometros = 0
tiempo = 0
velocidad = 0

kilometros = float(input("Ingrese la cantidad de kilometros recorridos: "))
tiempo = float(input("Ingrese los minutos que transcurrieron: "))

velocidad = kilometros / tiempo

if velocidad >= 0 and velocidad <= 0.1999:
    print("La velocidad de: ",kilometros,"KM/",tiempo,"m es lenta")

elif velocidad >= 0.2 and velocidad <= 0.3:
    print("La velocidad de: ",kilometros,"KM/",tiempo,"m es moderada")

else:
    print("La velocidad de: ",kilometros,"KM/",tiempo,"m es rapida")

print("Fin Del Programa")