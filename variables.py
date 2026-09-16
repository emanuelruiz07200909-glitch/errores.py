# ============================================================
# INTRODUCCIÓN A LAS VARIABLES EN PYTHON
# ============================================================

# Una variable permite almacenar un dato para utilizarlo
# posteriormente dentro del programa.

nombre = "Emanuel"
documento = 456789
direccion = "cr 23 # 45 - 34"
tiene_deuda = True  #Variable Booleano : true o false

# ============================================================
# MOSTRAR EL CONTENIDO DE UNA VARIABLE
# ============================================================

print(nombre)

print("CONCATENACIÓN USANDO +")
print("=" * 30)


print("Mi nombre es: " +  nombre + " Mi documento es: " + str(documento) )

# ============================================================
# CONCATENACIÓN USANDO ,
# ============================================================
print("\nCONCATENACIÓN USANDO ,")
print("=" * 30)

# Al utilizar comas, Python permite mostrar diferentes
# tipos de datos sin necesidad de convertirlos a string.
print("Mi nombre es:", nombre, "Mi documento es:", documento)

#Tarea: Mostrar nombre, documento, direccion y tiene_deuda
print("Mi nombre es: ", nombre, "Mi documento es: ", documento, "Mi direccion es: ", direccion, "¿Deuda?: ", tiene_deuda )

# ============================================================
# CONCATENACIÓN USANDO F-STRINGS
# ============================================================
print("\nCONCATENACIÓN USANDO F-STRINGS")
print("=" * 30)

# Las f-strings permiten insertar variables directamente
# dentro de un texto.
#
# Se coloca la letra f antes de las comillas y las variables
# se escriben entre llaves { }.

print(f"Mi nombre es: {nombre}")

print(f"Mi nombre es: {nombre} Mi documento: {documento} Mi direccion: {direccion} ¿Deuda? {tiene_deuda}")

# ============================================================
# F-STRINGS CON VARIAS VARIABLES
# ====================================================

print("\nMOSTRAR VARIAS VARIABLES CON F-STRINGS")
print("=" * 30)

# Las f-strings también permiten crear textos
# de varias líneas utilizando triple comilla.

print(f"""  
Nombre: {nombre}
Documento:{documento}    
Direccion: {direccion}   
¿Tiene Deudas?: {tiene_deuda}
 """)


