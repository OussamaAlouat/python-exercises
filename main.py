 #version: 0.2.0

from exercises.exercise1 import exercise1
from exercises.exercise2 import exercise2

exercises = [exercise1, exercise2]
print('Welcome to the python exercises repository')
print('##########################################')

for exercise in exercises:
  exercise()
  print('##########################################')
