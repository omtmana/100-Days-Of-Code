# Control Flow and Logical Operations

# if condition:
#  do this
# else:
#  do this

water_level = 50
if water_level > 80:
    print("Drain Water")
else:
    print("Continue")

# Checkout draw.io

# You need to be 120 cm to ride
# Condition if you can or cannot ride
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
   print("You can ride the rollercoaster!")
else:
   print("You can't ride the rollercoaster")

# Checking if the number is even or odd
number = int(input("Which number do you want to check? "))

if number % 2 == 0:
   print("This is an even number")
else:
   print("This is an odd number.")

# Nested if statements and elif statements
if condition:
   if another condition:
      do this # for this to happen first and second if condition has to be true
   else:
      do this # for this to happen first if has to be true second if has to be false
else:
   do this # for this to happen first and second if statements has to be false


# We need to check their height and also age
print("Welcome to the Rollercoaster")
height = int(input("What is your height in cm"))

if height >= 120:
   print("You can ride the rollercoaster")
   age = int(input("What is your age?"))
   if age <= 18:
      print("Please pay $7.")
   else:
      print("Please pay $12.")
else:
   print("Sorry you have to grow taller before you can ride.")

# if / elif / else
if condition1:
   do A # if condition1 is true this happens
elif condition2:
   do B # if condition1 is false and condition2 is true, then this happens
elif condition3:
   do C # if condition1 and 2 are false, then this happens
else:
   do this # if condition1, 2, and 3 are false, then this happens
   