# ------------------------------------------------------------------------------
# 🔹 5. Conversión de millas a kilómetros y metros
#
# Desarrolla un programa que convierta una cantidad dada en millas a su
# equivalente en kilómetros y metros.
# ------------------------------------------------------------------------------

# Define la relación de conversión
millas_a_kilometros = 1.60934
kilometros_a_metros = 1000

# Pide al usuario la cantidad en millas
millas_str = input("Mete la cantidad en millas: ")

try:
  # Intenta convertir la entrada del usuario a un número decimal
  millas = float(millas_str)

  # Verifica si la cantidad de millas es positiva
  if millas >= 0:
    # Calcula el equivalente en kilómetros
    kilometros = millas * millas_a_kilometros
    # Calcula el equivalente en metros
    metros = kilometros * kilometros_a_metros

    # Muestra los resultados
    print(f"{millas} millas son:")
    print(f"- {round(kilometros, 2)} kilómetros")
    print(f"- {round(metros, 2)} metros")
  else:
    # Si la cantidad de millas no es positiva, muestra un mensaje
    print("Por favor, mete una cantidad de millas positiva.")

except ValueError:
  # Si el usuario ingresa algo que no es un número, muestra un error
  print("Por favor, mete un número para la cantidad de millas.")