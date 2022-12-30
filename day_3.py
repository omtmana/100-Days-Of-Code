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
