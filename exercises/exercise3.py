'''
Diseña un programa que, a partir del valor de los dos lados de un rectángulo (4 y 6
metros, respectivamente)
(El perímetro debe darte 20 metros y el área 24 metros cuadrados).
'''

firstSide = 4
secondSide = 6

def __calculateRectangleArea(firstSide, secondSide):
  return firstSide * secondSide

def __calculateRectanglePerimeter(firstSide, secondSide):
  return 2*(firstSide + secondSide)

def exercise3():
    perimeter = __calculateRectanglePerimeter(firstSide, secondSide)
    area = __calculateRectangleArea(firstSide, secondSide)
    print('# Excercise 3: ')
    print('The perimeter is: ', perimeter, 'm')
    print('The area is: ', area, ' m2')
