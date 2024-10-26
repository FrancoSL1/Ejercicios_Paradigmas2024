#Ejercicio 6: Números pares e impares
numeros = 0
seguir = "si"
par = 0
impar = 0

while seguir == "si":
    numeros = int(input("Ingrese un número: "))

    if numeros % 2 == 0:
        par = par+1
    else:
        impar = impar+1
    
    seguir = input("¿Desea seguir? si o no: ")

print("La cantidad total pares e impares es: ", par + impar)
print("La cantidad de números pares es: ", par)
print("La cantidad de números impares es: ", impar)