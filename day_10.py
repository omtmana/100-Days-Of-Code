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
   return f"{title_first_name} {title_last_name}"

# Completed Version
# Functions with Outputs


def format_name(f_name, l_name):
  if f_name == "" or l_name == "":
    return "You didn't provide valid inputs."
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()
  f"Result: {formated_f_name} {formated_l_name}"


# Storing output in a variable
formatted_name = format_name(
    input("Your first name: "), input("Your last name: "))
print(formatted_name)
# or printing output directly
print(format_name(input("What is your first name? "),
      input("What is your last name? ")))

# Already used functions with outputs.
length = len(formatted_name)

# Return as an early exit


def format_name(f_name, l_name):
  """Take a first and last name and format it 
  to return the title case version of the name."""
  if f_name == "" or l_name == "":
    return "You didn't provide valid inputs."
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()
  return f"Result: {formated_f_name} {formated_l_name}"


# Docstrings
# This is a way for you to be able to document your functions
# This goes under the first line of delaring a function
def my_function(first_name, last_name):
   """Take a first and last name and format it 
   to return the title case version of the name."""
   if first_name == "" or last_name == "":
      return "You didn't provide valid inputs"
   formated_f_name = first_name.title()
   formatted_l_name = last_name.title()
   return f"Result: {formated_f_name} {formatted_l_name}"

