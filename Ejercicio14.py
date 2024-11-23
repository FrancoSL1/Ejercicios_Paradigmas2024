#Ejercicio 14, rendimiento de una carrera de autos
# Función para registrar los tiempos de vuelta de un auto
def registrar_tiempos(autos):
    while True:
        # Pedimos el número de identificación del auto
        id_auto = input("Ingresa el número de identificación del auto (o 'fin' para terminar): ")
        
        if id_auto.lower() == 'fin':
            break
        
        # Si el auto ya existe, se registran sus tiempos, si no, se crea un nuevo registro
        if id_auto in autos:
            print(f"El auto {id_auto} ya tiene registros de tiempos. Agregue una nueva vuelta.")
        else:
            autos[id_auto] = []
        
        # Registrar tiempos de vuelta
        while True:
            try:
                tiempo_vuelta = float(input(f"Ingrese el tiempo de vuelta (segundos) para el auto {id_auto}: "))
                autos[id_auto].append(tiempo_vuelta)
                otra_vuelta = input("¿Registrar otro tiempo para este auto? (s/n): ")
                if otra_vuelta.lower() != 's':
                    break
            except ValueError:
                print("Por favor ingrese un valor numérico válido para el tiempo de vuelta.")

# Función para calcular el tiempo promedio de un auto
def calcular_promedio(id_auto, autos):
    if id_auto in autos and len(autos[id_auto]) > 0:
        promedio = sum(autos[id_auto]) / len(autos[id_auto])
        return promedio
    else:
        print(f"El auto {id_auto} no tiene tiempos registrados.")
        return None

# Función para determinar el auto más rápido
def auto_mas_rapido(autos):
    auto_rapido = None
    mejor_tiempo = float('inf')
    
    for id_auto, tiempos in autos.items():
        promedio = calcular_promedio(id_auto, autos)
        if promedio is not None and promedio < mejor_tiempo:
            mejor_tiempo = promedio
            auto_rapido = id_auto
    
    if auto_rapido:
        print(f"El auto más rápido es el {auto_rapido} con un tiempo promedio de {mejor_tiempo:.2f} segundos.")
    else:
        print("No hay autos con tiempos registrados para determinar el más rápido.")

# Función para mostrar el rendimiento de todos los autos
def mostrar_rendimiento(autos):
    if not autos:
        print("No se han registrado autos aún.")
        return
    
    print("\nRendimiento de todos los autos:")
    for id_auto, tiempos in autos.items():
        print(f"\nAuto {id_auto}:")
        print(f"Tiempos de vuelta registrados: {', '.join(map(str, tiempos))}")
        promedio = calcular_promedio(id_auto, autos)
        if promedio is not None:
            print(f"Tiempo promedio de vuelta: {promedio:.2f} segundos")

# Función principal
def main():
    autos = {}
    
    while True:
        print("\nMenú de opciones:")
        print("1. Registrar tiempos de vuelta")
        print("2. Calcular tiempo promedio de un auto")
        print("3. Ver el auto más rápido")
        print("4. Mostrar rendimiento de todos los autos")
        print("5. Salir")
        
        opcion = input("Elija una opción (1-5): ")
        
        if opcion == '1':
            registrar_tiempos(autos)
        elif opcion == '2':
            id_auto = input("Ingrese el número de identificación del auto: ")
            promedio = calcular_promedio(id_auto, autos)
            if promedio is not None:
                print(f"El tiempo promedio de vuelta del auto {id_auto} es: {promedio:.2f} segundos")
        elif opcion == '3':
            auto_mas_rapido(autos)
        elif opcion == '4':
            mostrar_rendimiento(autos)
        elif opcion == '5':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, por favor elija una opción entre 1 y 5.")

if __name__ == "__main__":
    main()
