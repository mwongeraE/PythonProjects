def reverse(text):
  stringg = ''
  x=len(text)
  while (x>0):
    stringg = stringg + text[x - 1]
    x=x-1
  return stringg
