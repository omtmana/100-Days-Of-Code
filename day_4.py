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