'''
Diseña un programa que, a partir del valor de la base y de la altura de un triángulo
(3 y 5 metros, respectivamente), muestre el valor de su área (en metros cuadrados).
Recuerda que el área A de un triángulo se puede calcular a partir de la base  y la altura
 como A = 0.5 base * height
(El resultado es 7.5 metros cuadrados).
'''

base = 3
height = 5

def __calculateTriangleArea(base, height):
  return (base * height) / 2

def exercise2():
  area  = __calculateTriangleArea(base, height)
  print('# Excercise 2: ')
  print('The triangle area is: ', area)
