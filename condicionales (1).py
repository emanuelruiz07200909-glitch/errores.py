
"""
#Repaso clase pasada
var_nombre = input("Por favor ingrese su nombre")

var_edad = int(input(f"{var_nombre} Por favor ingresa tu edad: "))

#Validar si la edad es > = 18. y mostrar un mensaje qued diga que es mayor

if var_edad >= 18:
    print(f"{var_nombre} usted es mayor de edad")

else:
    print(f"{var_nombre} usted es menor de edad")
"""
"""
    # Ejercicio 1: Determinar si un número es positivo, negativo o cero
    
numero = float(input("ingrese un numero: "))
    
if numero > 0:
    print(f"El numero : {numero} es positivo")
         
elif numero < 0:
    print(f"El numero : {numero} es negativo")
             
else:        
    print(f"El numero : {numero} es cero")

# Ejercicio 3: Determinar si un número es par o impar

numero = int(input("Por favor ingrese un número: "))

if numero % 2 != 0: # si el residuo es 0 → es par
    print(f"El número {numero} es impar")
else:
    print(f"El número {numero} es par")
    
    # Ejercicio 4: Clasificar una nota académica
    
nota = float(input("Ingrese la nota obtenida (0.0 a 5.0): "))
    
if nota > 5.0:
    print(f"{nota} invalida")
elif nota >= 4.5:
    print("Desempeño Superior")
elif nota >= 3.5:
    print ("Desempeño alto")
elif nota >= 3.0:
    print("Desempeño básico")
elif nota >= 0:
    print("Desempeño bajo")
else:
    print("nota invalida")

# Ejercicio 5: Determinar el mayor de tres números
n1 = float(input("Ingrese el primer número: "))
n2 = float(input("Ingrese el segundo número: "))
n3 = float(input("Ingrese el tercer número: "))
if  n1== n2 and n1==n3:
    mayor = "Números iguales"
elif n1 >= n2 and n1 >= n3:
    mayor = n1
elif n2 >= n1 and n2 >= n3:
    mayor = n2   
else:
    mayor = n3
print(f"El mayor de los tres  números es: {mayor}")
"""
# Ejercicio 2
print("Notas Finales de los estudiantes")

variable_nombre= input("Por favor ingrese su nombre: ")
var_calificacion= float(input("Ingrese su calificación: "))
if var_calificacion >= 4.5 and var_calificacion <= 5.0:
    resultado = "Aprobó"
    desempeño = "Excelente"
    print(f"Estudiante: {variable_nombre} | Calificación: {var_calificacion} | Resultado: {resultado} | Desempeño: {desempeño}")
elif var_calificacion >= 3.5 and var_calificacion < 4.5:
    resultado = "Aprobó"
    desempeño = "Bueno"
    print(f"Estudiante: {variable_nombre} | Calificación: {var_calificacion} | Resultado: {resultado} | Desempeño: {desempeño}")
elif var_calificacion >= 3.0 and var_calificacion < 3.5:
    resultado = "Aprobó"
    desempeño = "Aceptable"
    print(f"Estudiante: {variable_nombre} | Calificación: {var_calificacion} | Resultado: {resultado} | Desempeño: {desempeño}")
elif var_calificacion >=0.0 and var_calificacion < 3.0:
    resultado = "Reprobó"
    desempeño = "Insuficiente"
    print(f"Estudiante: {variable_nombre} | Calificación: {var_calificacion} | Resultado: {resultado} | Desempeño: {desempeño}")
else: 
    print(f"{var_calificacion} es inválida")
    
  
    


        