# ------------------------------------------------------------------------------
# 🔹 3. Perímetro y área de un rectángulo
#
# Escribe un programa que calcule el perímetro y el área de un rectángulo,
# dados su largo y ancho. El programa debe validar que ambos valores
# sean positivos.
# ------------------------------------------------------------------------------

# Pide al usuario el largo del rectángulo
largo_str = input("Mete el largo del rectángulo: ")

# Pide al usuario el ancho del rectángulo
ancho_str = input("Mete el ancho del rectángulo: ")

# Intenta convertir el largo y el ancho a números decimales
try:
  largo = float(largo_str)
  ancho = float(ancho_str)

  # Verifica si ambos valores son positivos
  if largo > 0 and ancho > 0:
    # Calcula el área
    area = largo * ancho
    # Calcula el perímetro
    perimetro = 2 * (largo + ancho)
    # Muestra los resultados
    print("El área del rectángulo es:", round(area, 2))
    print("El perímetro del rectángulo es:", round(perimetro, 2))
  else:
    # Si el largo o el ancho no son positivos, muestra un error
    print("El largo y el ancho deben ser números positivos.")

except ValueError:
  # Si el usuario ingresa algo que no es un número, muestra un error
  print("Por favor, mete números para el largo y el ancho.")