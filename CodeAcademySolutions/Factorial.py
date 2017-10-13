def factorial(x):
  if x == 0 or x == 1:
    print 1
    return 1
  else:
    return x*factorial(x - 1)
