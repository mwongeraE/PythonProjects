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
