'''
 Ejercicio 1: Diseña un programa que, a partir del valor del lado de un cuadrado (3 metros),
 muestre el valor de su perímetro (en metros) y el de su área (en metros cuadrados).
(El perímetro debe darte 12 metros y el área 9 metros cuadrados).
'''

from math import pi

def calculatePerimeter(value):
    return value * 4

def calculateArea(value):
    return value * value

def exercice1():
    squareSade = 3
    perimeter = calculatePerimeter(squareSade)
    area = calculateArea(squareSade)
    print('# Excercice 1: ')
    print('The perimeter is: ', perimeter)
    print('The area is: ', area)
