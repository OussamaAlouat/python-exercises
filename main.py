 #version: 0.2.0

from exercises.exercise1 import exercise1
from exercises.exercise2 import exercise2
from exercises.exercise3 import exercise3

exercises = [exercise1, exercise2, exercise3]
print('Welcome to the python exercises repository')
print('##########################################')

for exercise in exercises:
  exercise()
  print('##########################################')
