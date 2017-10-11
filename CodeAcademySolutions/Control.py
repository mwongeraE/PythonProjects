#### For in Lists
names = ["Adam","Alex","Mariah","Martine","Columbus"]
for x in names:
  print x

####for in Dictionaries
webster = {
  "Aardvark" : "A star of a popular children's cartoon show.",
  "Baa" : "The sound a goat makes.",
  "Carpet": "Goes on the floor.",
  "Dab": "A small amount."
}

# Add your code below!
for key in webster:
  print webster[key]

#### Control flow and looping
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

for x in a:
  if x % 2 == 0:
    print x
