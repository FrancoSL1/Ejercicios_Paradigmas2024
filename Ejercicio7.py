#Ejercicio 7: Mesas disponibles en un restaurante
grupo = 0
seguir = "si"

print("***************************")
print("*Bienvenido al restaurante*")
print("***************************")

while seguir == "si":
    grupo = int(input("Ingrese el número de personas: "))

    if grupo > 1 and grupo < 3:
        print("*****************************")
        print("*Hay mesa para dos personas.*") 
        print("*****************************")
    elif grupo > 3 and grupo < 5:
        print("*****************************")
        print("*Hay mesa para cuatro personas.*") 
        print("*****************************")
    elif grupo > 5 and grupo < 7:
        print("******************************")
        print("*Hay mesa para seis personas.*") 
        print("******************************")
    elif grupo > 7 and grupo < 9:
        print("******************************")
        print("*Hay mesa para ocho personas.*") 
        print("******************************")
    else:
        print("No hay mesas para ese grupo.")
    
    seguir = input("¿Desea seguir? si o no: ")

print("Fin Del Programa")