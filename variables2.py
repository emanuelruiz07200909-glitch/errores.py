# Ejercicio 1: Suma de dos números
print("=="*30)

print("Ejercicio 1: Suma de dos números")

numero1=float(input("Ingrese el primer número: "))
numero2=float(input("Ingrese el segundo número: "))
suma = numero1 + numero2 

print(f"la suma es: {suma}")

print("=="*30) 

# Ejercicio 2: Área de un rectángulo
print("Ejercicio 2: Área de un rectángulo") 

base   = float (input("Ingrese la base del rectangulo: "))
altura = float(input("Ingrese la altura del rectángulo: "))

area = base * altura  # fórmula: base * altura

print("El área del rectángulo es:", area)

print("=="*30) 

# Ejercicio 3: Conversión de minutos a horas y minutos
print("Ejercicio 3: Minutos a horas y minutos")

minutos_totales = int(input("Ingrese la cantidad de minutos: "))

horas = minutos_totales // 60 # división entera → horas completas
minutos = minutos_totales % 60 # módulo → minutos restantes
print(minutos_totales, "minutos equivalen a", horas, "horas y", 
      minutos, "minutos")

print("=="*30)

# Ejercicio 4: Cálculo del precio con descuento
print("Ejercicio 4: Cálculo del precio con descuento")

precio = float(input("Ingrese el precio del producto: "))
descuento = float(input("Ingrese el porcentaje de descuento: "))
valor_descuento = precio * (descuento / 100) # Valor que se descuenta
precio_final = precio - valor_descuento #precio con descuento
print("El precio final a pagar es:", precio_final)

print("=="*30)

# Ejercicio 5: Intercambio de valores entre dos variables
print("Ejercicio 5: Intercambio de valores entre dos variables")

a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))

auxiliar = a # guardar temporalmente el valor de a
a = b  # a toma el valor de b
b = auxiliar # b toma el valor original de a

print ("Después del intercambio: a=", a, ", b=", b)

print("=="*30)

# Ejercicios para resolver
print( "Ejercicio 1: Calcular perimetro de terreno rectangular")

largo = float (input("Ingrese la base"))
ancho = float (input("Ingrese la altura"))

perimetro = base * altura

print("=="*30)

print("Ejercicio 2: Calcular promedio de notas")

nota1 = float(input("Ingrese nota1: "))
nota2 = float(input("Ingrese  nota2: "))
nota3 = float(input("Ingrese nota3: "))

promedio = (nota1+nota2+nota3)/3

print("=="*30)

print("Ejercicio 3: Nombre,edad y presentación de persona")

nombre = (input("Ingrese su nombre: "))
edad = (input("Ingrese su edad: "))

