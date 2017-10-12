num = 1

while num <= 10:  # Fill in the condition
  # Print num squared
  print num ** 2
  # Increment num (make sure to do this!)
  num += 1


#### Simple Errors
choice = raw_input('Enjoying the course? (y/n)')

while choice != 'y' and choice != 'n':  # Fill in the condition (before the colon)
  choice = raw_input("Sorry, I didn't catch that. Enter again: ")

#### Infinite loops
count = 0

while count < 10: # Add a colon
  print count
  count += 1
  # Increment count

  #### Your own while
  from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)

guesses_left = 3
# Start your game!
while guesses_left > 0:
  guess = int(raw_input("Your guess: "))
  if guess == random_number:
    print "You win"
    break
    guesses_left -= 1

else:
  print "You lose."

  #### for loop strings
  thing = "spam!"

for c in thing:
  print c

word = "eggs!"

# Your code here!
for d in word:
  print d
