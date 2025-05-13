# ------------------------------------------------------------------------------
# 🔹 2. Conversión de temperatura (Celsius a Fahrenheit o Fahrenheit a Celsius)
#
# Crea un programa que convierta una temperatura de Celsius a Fahrenheit
# o de Fahrenheit a Celsius, dependiendo de la elección del usuario.
# ------------------------------------------------------------------------------
def celsius_a_fahrenheit(celsius):
  """Convierte grados Celsius a grados Fahrenheit."""
  fahrenheit = (celsius * 9/5) + 32
  return fahrenheit

def fahrenheit_a_celsius(fahrenheit):
  """Convierte grados Fahrenheit a grados Celsius."""
  celsius = (fahrenheit - 32) * 5/9
  return celsius

# Pregunta al usuario qué conversión quiere hacer
opcion = input("¿Quieres convertir a (C)elsius o (F)ahrenheit?: ").upper()

if opcion == 'C':
  # El usuario quiere convertir a Celsius
  temp_f = float(input("Mete la temperatura en Fahrenheit: "))
  temp_c = fahrenheit_a_celsius(temp_f)
  print("En Celsius son:", round(temp_c, 2), "grados")
elif opcion == 'F':
  # El usuario quiere convertir a Fahrenheit
  temp_c = float(input("Mete la temperatura en Celsius: "))
  temp_f = celsius_a_fahrenheit(temp_c)
  print("En Fahrenheit son:", round(temp_f, 2), "grados")
else:
  # El usuario no metió ni C ni F
  print("No entendí. Por favor, escribe 'C' o 'F'.")