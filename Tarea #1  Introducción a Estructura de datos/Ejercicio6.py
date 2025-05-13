# ------------------------------------------------------------------------------
# 🔹 6. Calcular interés compuesto
#
# Escribe un programa que permita calcular el interés compuesto de un
# capital inicial, una tasa de interés anual y un número de años.
# ------------------------------------------------------------------------------

# Pide al usuario el capital inicial
capital_inicial_str = input("Mete el capital inicial (dinero inicial): ")

# Pide al usuario la tasa de interés anual (en porcentaje)
tasa_interes_str = input("Mete la tasa de interés anual (porcentaje, ejemplo: 5 para 5%): ")

# Pide al usuario el número de años
num_anios_str = input("Mete el número de años: ")

try:
  # Convierte las entradas a números
  capital_inicial = float(capital_inicial_str)
  tasa_interes_anual = float(tasa_interes_str) / 100  # Divide por 100 para tener la tasa decimal
  num_anios = int(num_anios_str)

  # Verifica que las entradas sean válidas (capital y años positivos)
  if capital_inicial >= 0 and num_anios >= 0:
    # Calcula el capital final usando la fórmula del interés compuesto
    capital_final = capital_inicial * (1 + tasa_interes_anual) ** num_anios

    # Calcula el interés ganado
    interes_ganado = capital_final - capital_inicial

    # Muestra los resultados
    print("\nResultados del interés compuesto:")
    print(f"Capital inicial: {round(capital_inicial, 2)}")
    print(f"Tasa de interés anual: {tasa_interes_anual * 100}%")
    print(f"Número de años: {num_anios}")
    print(f"Capital final después de {num_anios} años: {round(capital_final, 2)}")
    print(f"Interés total ganado: {round(interes_ganado, 2)}")

  else:
    print("Por favor, mete un capital inicial y un número de años no negativos.")

except ValueError:
  print("Por favor, mete números válidos para el capital, la tasa de interés y el número de años.")
  