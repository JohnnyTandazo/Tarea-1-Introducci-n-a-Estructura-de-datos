### 🔹 **1. Área y perímetro de un círculo**

##Escribe un programa que calcule el **área** y el **perímetro** de un círculo, dado el valor de su radio. 
# El programa debe validar que el radio sea un valor positivo.

import math  # Trae las herramientas de matemáticas

radio = float(input("Mete el radio del círculo aquí: "))  # Pide el radio y lo guarda como número

if radio > 0:  # Si el radio es más grande que cero:
  area = math.pi * radio * radio  # Calcula el área (pi por radio por radio)
  perimetro = 2 * math.pi * radio  # Calcula la vuelta (2 por pi por radio)
  print("El área es:", round(area, 2))  # Muestra el área con dos decimales
  print("La vuelta es:", round(perimetro, 2))  # Muestra la vuelta con dos decimales
else:  # Si el radio NO es más grande que cero:
  print("El radio tiene que ser un número positivo.")  # Muestra un mensaje de error