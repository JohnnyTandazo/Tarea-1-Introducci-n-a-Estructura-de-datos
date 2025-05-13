# ------------------------------------------------------------------------------
# 🔹 4. Potencia de un número con opción de repetir
#
# Crea un programa que calcule la potencia de un número, dados una base
# y un exponente ingresados por el usuario. El programa debe permitir
# al usuario realizar múltiples cálculos sin reiniciar.
# ------------------------------------------------------------------------------

while True:  # Repite el siguiente bloque de código hasta que se le diga que pare
  # Pide al usuario la base
  base_str = input("Mete la base (un número): ")
  # Pide al usuario el exponente
  exponente_str = input("Mete el exponente (un número entero): ")

  try:
    base = float(base_str)
    exponente = int(exponente_str)  # Los exponentes suelen ser enteros

    # Calcula la potencia
    resultado = base ** exponente

    # Muestra el resultado
    print(f"{base} elevado a la potencia de {exponente} es: {resultado}")

  except ValueError:
    print("Por favor, mete un número para la base y un número entero para el exponente.")

  # Pregunta al usuario si quiere hacer otro cálculo
  otra_vez = input("¿Quieres calcular otra potencia? (sí/no): ").lower()
  if otra_vez != 'sí':
    break  # Sale del bucle 'while' si el usuario no escribe 'sí'

print("¡Gracias por usar la calculadora de potencias!")