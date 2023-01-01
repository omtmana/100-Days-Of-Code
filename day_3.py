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


# There are different prices for different ages too! account for that pls
print("Welcome to the Rollercoaster")
height = int(input("What is your height in cm"))

if height >= 120:
   print("You can ride the rollercoaster")
   age = int(input("What is your age?"))
   if age < 12:
      print("Please pay $5")
   elif age <= 18:
      print("Please pay $7")
   else:
      print("Please pay $12")
else:
   print("Sorry, you have to grow taller before you can ride.")

# Checking for BMI
height = float(input("What is your height in m? "))
weight = float(input("What is your height in km? "))

bmi = round(weight / (height ** 2))

if bmi < 18.5:
   print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
   print(f"Your BMI is {bmi}, you are a normal weight.")
elif bmi < 30:
   print(f"Your BMI is {bmi}, you are obese.")
elif bmi < 35:
   print(f"Your BMI is {bmi}, you are obese")
else:
   print(f"Your BMI is {bmi}, you are clinically obese")

# Adding my method of code for this challenge
# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
bmi = int(round(weight / (height ** 2)))

# conditionals to print dif. responses
if bmi >= 35:
    print(f"Your BMI is {bmi}, you are clinically obese.")
elif bmi in range(30, 35):
    print(f"Your BMI is {bmi}, you are obese.")
elif bmi in range(25, 30):
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi in range(int(18.5), 25):
    print(f"Your BMI is {bmi}, you have a normal weight.")
else:
    print(f"Your BMI is {bmi}, you are underweight.")

# Leap year or Not leap year
year = int(input("What year do you want to check?"))

if year % 4 == 0:
   if year % 100 == 0:
      if year % 400 == 0:
         print("Leap Year")
      else:
         print("Not leap year")
   else:
      print("Leap Year")
else:
   print("Not leap year")

# Recap
if condition1: # if this is true, then do A will happen and that's it
   do A  
elif condition2:
   do B
else:
   do C

# Multiple if
if condition1: #if true do this
   do A
if condition2: # if true will do this too
   do B
if condition3: # if true will do this as well
   do C

# Multiple If statements example
print("Welcome to my Rollercoaster!")
height = int(input("What is your height in cm?"))
bill = 0

if height >= 120:
   print("You can ride the rollercoaster!")
   age = int(input("What is your age?"))

   if age < 12:
      print("Please pay $5")
      bill = 5
   elif age <= 18:
      print("Please pay $7")
      bill = 7
   else:
      print("Please pay $12")

   ticket_purchase = input("Do you want to purchase a ticket for $3? Y or N")

   if ticket_purchase == "Y":
      # bill = bill + 3
      bill += 3
      print(f"Your bill is ${bill}")
   
else:
   print("Sorry, you have to grow taller before you can ride")