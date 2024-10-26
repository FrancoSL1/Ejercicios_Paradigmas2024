#Ejercicio 9: Juego de Adivinanza
import random 

numsc = random.randrange(1,100)
numUno = 0

print("ADIVINE UN NÚMERO DEL 1 AL 100")

for i in range(10):
    print(f"Intento N°{i+1}")
    numUno = int(input("ingrese un número: "))
    
    if numUno > numsc:
        print("Es mayor al número.")
    elif numUno < numsc:
        print("Es menor al número.")

    if numUno == numsc:
        break
  
if numUno == numsc:
    print("\n ¡FELICIDADES ADIVINO EL NÚMERO! \n")
    print(f"Número de intentos: {i+1}")
else:
    print(f"\n Perdiste el número secreto es: {numsc} \n")

print("Fin del programa")