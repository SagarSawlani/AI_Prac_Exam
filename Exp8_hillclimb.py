import random
# import math (for Trignometric function)

def f(x):
  return (-5*x*x + 3*x + 6) # math.sin(x) 

def hill_climbing():
  current_x = random.uniform(-10, 10) # (0, 6.28) for y=sinx (0 to 2pi)

  step = 0.1
  while True:
    left = current_x - step
    right = current_x + step

    if f(left) > f(current_x):
      current_x = left
    elif f(right) > f(current_x):
      current_x = right
    else:
      break

  return current_x, f(current_x)

x, y = hill_climbing()

print("Reached Peak at x = ", x, "\nFitness: ", y)