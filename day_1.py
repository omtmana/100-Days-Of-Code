# ********* Print function ********
#  print() function

print('Hello World!')

# Interactice Code Challenge (Printing)
print('Day 1- Python Print Function')
print('The function is declared like this:')
print("print('what to print')")

# Printing 3 times
print('Hello World!\nHello World!\nHello World')

# Concatinating two strings
print('Hello' + '' + 'Molly')

# Errors
# Syntax Erorr
# Indentation Error


# ********** Input Function ***********
# input() function
input("A prompt for the user")
input("What is your name?")

print("Hello " + input("What is your name?"))
# checkout Thonny.org

# Input : Angela
# Output : 6

print(len(input('What is your name? ')))

# ******** VARIABLES *******
name = input("What is your name")
print(name)

name = "Jack"
print(name)

name = "Angela"
print(name)

print(len(input('What is your name? ')))
name = input('What is your name? ')
length = len(name)
print(length)


# Input a : 1 b : 2
# Output a : 2 b : 1
a = input("a: ")
b = input("b: ")

storinga = a
storingb = b
a = storingb
b = storinga

print("a: " + a)
print("b: " + b)
