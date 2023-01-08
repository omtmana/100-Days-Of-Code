# Python Loops

# For Loop
for item in list_of_items:
   # Do something to each item

# A list with three items
fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
   print(fruit)

for fruit in fruits:
   print(fruit)
   print(fruit + "Pie")
   print(fruits)

# Average Height
# Find the average. The goal is to not use len() and sum()

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


# Write your code below this row 👇
sum = 0
num_of_height = len(student_heights)
for height in student_heights:
    sum += height
    total = round(sum / num_of_height)

print(total)

sum = 0
for height in student_heights:
    sum += height

num_of_students = 0
for student in student_heights:
    num_of_students += 1

total = round(sum / num_of_students)
print(total)


# Highest Score exercise
# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
highest_score = 0
for score in student_scores:
    if highest_score < score:
        highest_score = score

print(f"The highest score in the class is: {highest_score}")

# For loops and the range() function
for number in range(a, b):
    print(number)

# example (1 to 9, 10 doesnt get print out)
for number in range(1, 10, 3):
    print(number)

total = 0
for number in range(1, 101):
    total += number
print(total)

# Adding only the even numbers from 1-100
total = 0
for number in range(2, 101, 2):
    total += number
print(total)

total2 = 0
for number in range(1, 101):
    if number % 2 == 0:
        total2 += number
print(total2)

# FizzBuzz
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")