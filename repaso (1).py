
# REPASO CLASE PASADA
print("=== Tienda Merca + 🏪 ====\n")
#Solicitar Variables
producto = input("Ingrese el nombre del producto: ")
cantidad = int(input(f"Ingrese la cantidad a comprar: "))
precio = float(input("Ingrese el precio unitario del producto: "))

#Crear Variables 
subtotal = cantidad * precio
iva = subtotal * 0.19
total =subtotal + iva
print("\n === RESUMEN DE COMPRA === \n")
print(f"""
      -producto ...............{producto}
      -cantidad ...............{cantidad}
      -precio unitario ........{precio}
      -subtotal ...............{subtotal}
      -IVA (19%) ..............{iva}
      -total pagar ............{total}
      
      """)

#Preguntar si quiere incluir propina
propina = input("¿Desea incluir propina? : ")
if propina == "si" or propina =="SI" or propina =="Si" : 
    valor_propina = subtotal * 0.10
    total_final = total + valor_propina
    
    print(f"""
      -subtotal ...............{subtotal}
      -IVA (19%) ..............{iva}
      valor_propina(10%) ......{valor_propina}
      -total pagar ............{total_final}
""")
elif propina == "no" or propina == "NO" or propina == "No":
    print("Gracias por su compra TACAÑO CODO.")
else: 
     print("Opción no válida, por favor ingrese 'si' o 'no'")
     
