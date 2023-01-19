# Dictionaries and Nesting (list inside list)

# The Python Dictionaries
# Allow us to group together and tag related pieces of information
# Table: Key = Value e.g Loop = The action of doing something over and over again
{key: Value}
{
   "Bug": "An error in a program that prevents the program form running as expected",
   "print": "To print a message in Python"
}

programming_dictionary = {
   "Bug": "Something",
   "Function": "A piece of code that you can call over again",
   "Loop": "Action of doing something over and over again"
}

# Retrive items from a dictionary
programming_dictionary["Bug"]
print(programming_dictionary["Bug"])
dictionary_name["keyName"]

# Adding a Piece of data in dictionary
dictionary_name["keyName"] = "Value of the key you want to add"

# Create a new dictionary
empty_dictionary = {}
# empty_dictionary = []

# Wipe an existing dictionary
programming_dictionary = {}
print(programming_dictionary)

# Edit an item in a dictionary
programming_dictionary["Bug"] = "This is the redefined value from the key I fetched"

# Loop Through a dictionary
for thing in programming_dictionary:
   print(programming_dictionary[thing]) #this gives you the value

for key in programming_dictionary:
   print(key) # this gives you only the key in the dictionary

# Student Grades exercise
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# student_grades[student]
# TODO-2: Write your code below to add the grades to student_grades.👇
for student in student_scores:
    score = student_scores[student]
    if score < 70:
        student_grades[student] = 'Fail'
    elif score > 70 and score < 80:
        student_grades[student] = 'Acceptable'
    elif score > 80 and score < 90:
        student_grades[student] = "Exceeds Expectations"
    elif score > 91 and score < 100:
        student_grades[student] = 'Outstanding'


# 🚨 Don't change the code below 👇
print(student_grades)

# Nested
nested = {
   key: ['item1', 'item', 'item3'],
   key2: {
      key2a: 'value2a',
      key2b: 'value2b'
   },
}

# Sample dictionaries
capitals = {
   "France": "Paris",
   "Germany": "Berlin",
}

# Nesting a list in a dictionary
travel_log = {
   "France": ["Paris", "Lille", "Dijon"],
   "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

# Nesting a dictionary in a dictionary
travel_log = {
   'France': {
      'cities_visited': ['Paris', 'Lille', 'Dijon'],
      'total_visits': 12
   },
   "America": {
      'cities_visited': ['New York', 'San Francisco', 'Las Vegas'],
      'total_visits': 12
   }
}

 