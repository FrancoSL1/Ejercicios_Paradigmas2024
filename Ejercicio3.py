#Ejercicio 3: Selección de atuendo

#Variables
nombre = " "
temperatura = 0
lluvia = " "

#Ingreso de datos
nombre = (input("Ingrese su nombre: "))
temperatura = int(input("Ingrese la temperatura en grados Celsius: "))
lluvia = (input("¿Habrá lluvia?: "))

#procesos
if lluvia == "si":
    if temperatura <= 15:
        print(nombre,", deberias llevar un abrigo muy grueso para una temperatura de: ", temperatura,"°C")
        print("Se recomienda que lleves un paraguas para la lluvia.")

    elif temperatura >= 16 and temperatura <= 20:
        print(nombre,", debarias llevar una remera de mangas largar para una temperatura de: ", temperatura, "°C")
        print("Se recomienda que lleves un paraguas para la lluvia.")
    
    else: 
        print(nombre,", deberias solo llevar una remera para una temperatura de: ", temperatura,"°C")
        print("Se recomienda que lleves un paraguas para la lluvia.")

else:
    if temperatura < 15:
        print(nombre,", deberias llevar un abrigo muy grueso para una temperatura de: ", temperatura,"°C")

    elif temperatura >= 16 and temperatura <= 20:
        print(nombre,", debarias llevar una remera de mangas largar para una temperatura de: ", temperatura,"°C")
    
    else:
        print(nombre,", deberias solo llevar una remera para una temperatura de: ", temperatura,"°C")

print("Fin Del Programa")