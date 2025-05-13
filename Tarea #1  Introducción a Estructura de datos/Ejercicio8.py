# ------------------------------------------------------------------------------
# 🔹 8. Cálculo de descuento con validación
#
# Desarrolla un programa que calcule el precio final de un producto después
# de aplicarle un porcentaje de descuento. El programa debe validar que
# el porcentaje esté entre 0 y 100.
# ------------------------------------------------------------------------------

# Pide al usuario el precio original del producto
precio_original_str = input("Mete el precio original del producto: ")

# Pide al usuario el porcentaje de descuento
descuento_str = input("Mete el porcentaje de descuento (entre 0 y 100): ")

try:
  # Convierte las entradas a números
  precio_original = float(precio_original_str)
  porcentaje_descuento = float(descuento_str)

  # Valida el porcentaje de descuento
  if 0 <= porcentaje_descuento <= 100:
    # Calcula el descuento en valor
    descuento_valor = precio_original * (porcentaje_descuento / 100)
    # Calcula el precio final
    precio_final = precio_original - descuento_valor

    # Muestra los resultados
    print(f"\nPrecio original: {round(precio_original, 2)}")
    print(f"Porcentaje de descuento: {porcentaje_descuento}%")
    print(f"Descuento aplicado: {round(descuento_valor, 2)}")
    print(f"Precio final: {round(precio_final, 2)}")

  else:
    print("El porcentaje de descuento debe estar entre 0 y 100.")

except ValueError:
  print("Por favor, mete números válidos para el precio y el porcentaje de descuento.")