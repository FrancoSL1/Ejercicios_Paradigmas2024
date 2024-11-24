#Ejercicio 15: Análisis de muestras en un laboratorio químico
# Diccionario global para almacenar los datos de las muestras
# Cada clave será el identificador de la muestra, y su valor será otro diccionario
# con los elementos químicos como claves y listas de concentraciones como valores.
muestras = {}

# Función para registrar resultados de análisis
def registrar_muestra(id_muestra, elemento, concentracion):
    if id_muestra not in muestras:
        muestras[id_muestra] = {}
    if elemento not in muestras[id_muestra]:
        muestras[id_muestra][elemento] = []
    muestras[id_muestra][elemento].append(concentracion)
    print(f"Concentración de {concentracion} ppm de {elemento} registrada para la muestra {id_muestra}.")

# Función para calcular el promedio de concentración de un elemento en una muestra
def calcular_promedio(id_muestra, elemento):
    if id_muestra in muestras and elemento in muestras[id_muestra]:
        concentraciones = muestras[id_muestra][elemento]
        promedio = sum(concentraciones) / len(concentraciones)
        print(f"El promedio de concentración de {elemento} en la muestra {id_muestra} es {promedio:.2f} ppm.")
        return promedio
    else:
        print(f"No se encontraron datos para el elemento {elemento} en la muestra {id_muestra}.")
        return None

# Función para determinar la muestra con la mayor concentración promedio de un elemento
def muestra_con_mayor_promedio(elemento):
    mayor_promedio = -1
    muestra_mayor = None
    for id_muestra, elementos in muestras.items():
        if elemento in elementos:
            promedio = sum(elementos[elemento]) / len(elementos[elemento])
            if promedio > mayor_promedio:
                mayor_promedio = promedio
                muestra_mayor = id_muestra
    if muestra_mayor:
        print(f"La muestra con mayor concentración promedio de {elemento} es {muestra_mayor} con un promedio de {mayor_promedio:.2f} ppm.")
    else:
        print(f"No se encontraron datos del elemento {elemento} en ninguna muestra.")

# Función para mostrar todos los análisis registrados
def mostrar_analisis():
    if not muestras:
        print("No hay análisis registrados.")
        return
    for id_muestra, elementos in muestras.items():
        print(f"Muestra {id_muestra}:")
        for elemento, concentraciones in elementos.items():
            print(f"  {elemento}: {concentraciones}")

# Menú principal
def menu():
    while True:
        print("\n--- Menú ---")
        print("1. Registrar análisis")
        print("2. Calcular promedio de concentración")
        print("3. Muestra con mayor promedio de un elemento")
        print("4. Mostrar todos los análisis")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            id_muestra = input("Ingrese el identificador de la muestra: ")
            elemento = input("Ingrese el nombre del elemento: ")
            try:
                concentracion = float(input("Ingrese la concentración (ppm): "))
                registrar_muestra(id_muestra, elemento, concentracion)
            except ValueError:
                print("Por favor, ingrese un valor numérico válido para la concentración.")
        elif opcion == "2":
            id_muestra = input("Ingrese el identificador de la muestra: ")
            elemento = input("Ingrese el nombre del elemento: ")
            calcular_promedio(id_muestra, elemento)
        elif opcion == "3":
            elemento = input("Ingrese el nombre del elemento: ")
            muestra_con_mayor_promedio(elemento)
        elif opcion == "4":
            mostrar_analisis()
        elif opcion == "5":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el programa
menu()
