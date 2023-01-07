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
