'''
try:
    numero = int(input("Ingrese un número: "))
    print(f"El número ingresado: {numero}")
    
except ValueError:
        print("Ingrese un número válido")    
menu = 0
while menu != 3:
    try:
        menu = int(input("""
        Seleccione una opción:
        1. Sumar
        2. Restar
        3. Salir
            """))
        if menu ==1:
            n1=int(input("Ingrese Primer Número: "))
            n2=int(input("Ingrese Segundo Número: "))
            print(f"Resultado {n1+n2}")
        elif menu ==2:
            n1=int(input("Ingrese Primer Número: "))
            n2=int(input("Ingrese Segundo Número: "))
            print(f"Resultado {n1-n2}")

        else:
            print("Opción Invalida")
    except ValueError:
        print("Inserte un número valido")
print("Saliendo del sistema")
''
# Ejercicio 2: Division segura con ZeroDivisionError
try:
    dividendo = float(input("Ingrese el dividendo." ))
    divisor = float(input("Ingrese el divisor: "))
    resultado = dividendo / divisor
    print(f"Resultado: {dividendo} / {divisor} = {resultado}")
except ZeroDivisionError:
    print("Error: no es posible dividir entre cero.")
except ValueError:
    print("Error: ingrese únicamente valores numéricos.")

   # Ejercicio 3: else y finally
# else  → se ejecuta solo si NO ocurrió ninguna excepción
# finally → se ejecuta SIEMPRE, con o sin error
try:
    edad = int(input("Ingrese su edad: "))
except ValueError:
    print("Error: la edad debe ser un número entero.")
else:
    if edad >= 18:
        print("Acceso permitido.")
    else:
        print("Acceso denegado: debe ser mayor de edad.")
finally:
    print("Verificación finalizada.")

 # Ejercicio 4: Solicitar un dato válido hasta que el usuario lo ingrese correctamente
while True:
    try:
        nota = float(input("Ingrese una nota entre 0.0 y 5.0: "))
        if nota < 0.0 or nota > 5.0:
            raise ValueError("La nota debe estar entre 0.0 y 5.0.")
        break #Sale del ciclo si el valor es válido
    except ValueError as e:
        print(f"Entrada Inválida: {e}. Intente de nuevo.")
print(f"Nota registrada: {nota}")
'''
# Ejercicio 5: raise — lanzar una excepción personalizada
def calcular_promedio(notas):
    if len(notas) == 0:
        raise ValueError("La lista de notas no puede estar vacía.")
    return sum(notas) / len(notas)
try:
    n   = int(input("¿Cuántas notas va a ingresar? "))
    notas = []
    for i in range(n):
        nota = float(input(f" Nota {i + 1}: "))
        notas.append(nota)
        promedio = calcular_promedio(notas)
        print(f"Promedio: {round(promedio,2)}")
except ValueError as e:
    print(f"Error: {e}")