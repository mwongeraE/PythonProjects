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

#List Slicing
suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]

# The first and second items (index zero and one)
first = suitcase[0:2]

# Third and fourth items (index two and three)
middle = suitcase[2:4]

# The last two items (index four and five)
last =  suitcase[4:6]

#Maintaining order
animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index("duck")# Use index() to find "duck"

# Your code here!
animals.insert(duck_index, "cobra")

print animals # Observe what prints after the insert operation

#For loop in Lists
my_list = [1,9,3,8,5,7]

for number in my_list:
  # Your code here
  print 2*number

#More with 'for'
start_list = [5, 3, 1, 2, 4]
square_list = []

# Your code here!
for x in start_list:
  square = x ** 2
  square_list.append(square)
  square_list.sort()

print square_list

#### New entries Dictionary
menu = {} # Empty dictionary
menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
print menu['Chicken Alfredo']

# Your code here: Add some dish-price pairs to menu!
menu['Githeri'] = 3.00
menu['Pilau'] = 2.4
menu['Ugali'] = 5.5

print "There are " + str(len(menu)) + " items on the menu."
print menu

#### Deleting from Dictionary
# key - animal_name : value - location
zoo_animals = { 'Unicorn' : 'Cotton Candy House',
'Sloth' : 'Rainforest Exhibit',
'Bengal Tiger' : 'Jungle House',
'Atlantic Puffin' : 'Arctic Exhibit',
'Rockhopper Penguin' : 'Arctic Exhibit'}
# A dictionary (or list) declaration may break across multiple lines

# Removing the 'Unicorn' entry. (Unicorns are incredibly expensive.)
del zoo_animals['Unicorn']

# Your code here!
del zoo_animals['Sloth']
del zoo_animals['Bengal Tiger']

zoo_animals['Rockhopper Penguin'] = 'Cow'

print zoo_animals

#### Dictionaries Summary
inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort()

# Your code here
inventory['pocket'] = ['seashell', 'strange berry', 'lint']
inventory['pocket'].sort()
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
inventory['backpack'].sort()
inventory['gold'] = inventory['gold'] +50
