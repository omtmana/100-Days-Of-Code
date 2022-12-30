#  ******** Primitive Data Types *********

# Strings : String of Characters 
# Subscript : pulling a character from the string
print("Hello"[4])
print("123" + "456") #123456

# Interger (whole number w/o decimal places)
123 + 345
print(123 + 345) # 468
123_456_789 # it's like using commas

# Float (numbers with decimals)
3.14159

# Boolean
True
False

# Type Error - Type Checking - Type Conversion
# len() function doesn't work on integers

num_char = len(input("What is your name? "))
print("Your name has " + num_char) # this will produce an error

type(num_char)

# Challenge
# Input : 2 digit number
# Output : Sum of the digits

two_digit_number = input("Input a two digit number: ")

first_num = two_digit_number[0]
second_num = two_digit_number[1]

print(int(first_num) + int(second_num))

# Second Coding Challenge BMI
# Input : weight in kg, height it m
# Output : BMI = (weight / (height ** 2))

height = input("Input height in m: ")
weight = input("Input weight in kg: ")

# Convert input to either Float or Int to be able to mathematically combine them
height_float = float(height)
weight_int = int(weight)

# Solve then print
bmi = (weight_int / (height_float ** 2))
print(int(bmi))


