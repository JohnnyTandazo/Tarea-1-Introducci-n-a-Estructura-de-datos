# ------------------------------------------------------------------------------
# 🔹 7. Cálculo del promedio de N notas
#
# Crea un programa que permita ingresar un número indefinido de notas,
# y al finalizar, calcule el promedio de todas ellas.
# ------------------------------------------------------------------------------

notas = []  # Creamos una lista vacía para guardar las notas

print("Ingresa las notas. Escribe 'fin' cuando no quieras ingresar más.")

while True:
  nota_str = input("Mete una nota (o 'fin'): ")
  if nota_str.lower() == 'fin':
    break  # Si el usuario escribe 'fin', salimos del bucle

  try:
    nota = float(nota_str)
    if 0 <= nota <= 10:  # Suponiendo que las notas son entre 0 y 10
      notas.append(nota)  # Añadimos la nota a la lista
    else:
      print("La nota debe estar entre 0 y 10.")
  except ValueError:
    print("Por favor, mete un número para la nota o escribe 'fin'.")

if notas:  # Verificamos si hay al menos una nota en la lista
  promedio = sum(notas) / len(notas)  # Calculamos la suma de las notas y la dividimos por la cantidad
  print(f"\nEl promedio de las notas ingresadas es: {round(promedio, 2)}")
else:
  print("\nNo se ingresaron notas, por lo tanto no se puede calcular el promedio.")