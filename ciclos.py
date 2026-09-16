# INTRODUCCION A CICLOS:Ciclo for repite cantidades de veces
"""
mensaje = input("Que mensajes quieres mostrar: ")
cantidad = int(input("Cuantas veces quiere repetir el mensaje"))
for i in range(cantidad):
    print(f"{i} - 45")
# Ejercicio 1 Mostrar la tabla de multiplicar de un número
numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
for i in range(2,22):
    print(f"{numero} * {i} = {numero * i}")
    # Ejercicio 2: Sumar los primeros n números naturales
    n = int(input("Ingrese un numero entero positivo: "))
    suma = 0
    for i in range(1, n + 1):
        suma = suma + i
    print (f"La suma de los primeros {n} números naturales es: {suma}")

import random
numero_secreto = random.randint(1,10)
intentos = 3
for i in range(intentos):
 numero = int(input( "Adivina el número secreto: "))
 
 if numero == numero_secreto:
     print(" ¡Felicidades! Adivinaste el número.")
     break
 else:
     intentos_restantes =intentos -(i + 1)
     print(f"Te quedan {intentos_restantes} intentos.")
     if intentos_restantes == 0:
         print(f"El número era {numero_secreto}")
        """
         
import random
numero_secreto = random.randint(1,10)
intentos = 3
for i in range(intentos):
 numero = int(input( "Adivina el numero secreto: "))
 
 if numero == numero_secreto:
     print(" ¡Felicidades! Adivinaste el número.")
     break
 elif numero > numero_secreto:
     print("brutaa, es mayor que el numero secreto beba")
 elif numero < numero_secreto:
     print("Maldita retrasada, es menor que el numero secreto.")
 else:
     intentos_restantes =intentos -(i + 1)
     print(f"Te quedan {intentos_restantes} intentos.")
     if intentos_restantes == 0:
         print(f"El número era {numero_secreto}")