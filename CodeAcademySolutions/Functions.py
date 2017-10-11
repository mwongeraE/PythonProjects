def spam():
  """Prints 'Eggs!'"""
  print "Eggs!"

# Define the spam function above this line.
spam()

#Square function
def square(n):
  """Returns the square of a number."""
  squared = n ** 2
  print "%d squared is %d." % (n, squared)
  return squared

# Call the square function on line 10! Make sure to
# include the number 10 between the parentheses.
square(10)

#power function
def power(base,exponent):  # Add your parameters here!
  result = base ** exponent
  print "%d to the power of %d is %d." % (base, exponent, result)

power(37, 4)  # Add your arguments here!

#Functions calling Functions
def one_good_turn(n):
  return n + 1

def deserves_another(n):
  return one_good_turn(n) + 2

def cube(number):
  return number ** 3

#Cube function 6/19
def by_three(number):
  if number % 3 == 0:
  	return cube(number)
  else:
    return False

#import from module
import math # Imports the math module
everything = dir(math) # Sets everything to a list of things from math
print everything # Prints 'em all!

#Here be dragons
def biggest_number(*args):
  print max(args)
  return max(args)

def smallest_number(*args):
  print min(args)
  return min(args)

def distance_from_zero(arg):
  print abs(arg)
  return abs(arg)

biggest_number(-10, -5, 5, 10)
smallest_number(-10, -5, 5, 10)
distance_from_zero(-10)

#Reviewing Functions
def shut_down(s):
    if s == "yes":
        return "Shutting down"
    elif s == "no":
        return "Shutdown aborted"
    else:
        return "Sorry"
