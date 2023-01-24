# Day 10: Functions with outputs

# Recap
# Functions
def my_function():
   # Do this
   # Then this

my_function()

# Functions with Inputs with something as parameter
def my_function(something):
   # Do this with something
   # Then do this

my_function(123) # 123 is an argument to parameter something

# Now => Functions with outputs
# return keyword
def my_function():
   return 2 * 3

output = my_function():

# Example
def my_function(first_name, last_name):
   title_first_name = first_name.title()
   title_last_name = last_name.title()
   return "{title_first_name} {title_last_name}"
