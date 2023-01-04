import random
# Random
# askpython.com
# import random 


random_integer = random.randint(1, 10)
print(random_integer)

random_float = random.random()
print(random_float)

random_int_float = random_float * 5

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")

# Heads or Tails
zero_one = random.randint(0,1)

if zero_one == 1:
   print("Heads")
else:
   print("Tails")

# List
# variable : storing one piece of data
# Data Structure : way of organizing and storing group pieces of data
   # a way to store with order
fruits = [item1, item2, item3, item4, item5]
fruits = ["Cherry", "Apple", "Mango"]

# Before
state1 = "Delaware"
state2 = "New York"

# Now
states_of_america = ["Delaware", "New York", "California"]
print(states_of_america[0]) # Delaware
print(states_of_america[-1]) # California

#  Add at the end
states_of_america.append("MollyLand")
