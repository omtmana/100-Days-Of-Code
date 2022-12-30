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

