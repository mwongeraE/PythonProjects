zoo_animals = ["pangolin", "cassowary", "sloth", "cow" ];
# One animal is missing!

if len(zoo_animals) > 3:
  print "The first animal at the zoo is the " + zoo_animals[0]
  print "The second animal at the zoo is the " + zoo_animals[1]
  print "The third animal at the zoo is the " + zoo_animals[2]
  print "The fourth animal at the zoo is the " + zoo_animals[3]

#Index
zoo_animals = ["pangolin", "cassowary", "sloth", "tiger"]

# The ferocious sloth has been replaced by a friendly hyena.
zoo_animals[2] = "hyena"

# What shall fill the void left by our dear departed tiger?
# Your code here!
zoo_animals[3] = "cow"

#List Length and append
suitcase = []
suitcase.append("sunglasses")

# Your code here!
suitcase.append("Trouser")
suitcase.append("Shorts")
suitcase.append("Shirt")

list_length = len(suitcase) # Set this to the length of suitcase

print "There are %d items in the suitcase." % (list_length)
print suitcase
