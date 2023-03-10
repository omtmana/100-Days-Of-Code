# Functions

# Defining the Function
def my_function_name():
   # do this
   # then do this
   # finally do this

# Calling Functions
my_function_name()

# Functions are usefull because if you repeat
# instructions it can carry out the steps over and over again

# Reborgs World
def turn_right():
    turn_left()
    turn_left()
    turn_left()


def move_box():
    turn_left()
    move()


def up_and_down():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()


move()
up_and_down()
move_box()
up_and_down()
move_box()
up_and_down()
move_box()
up_and_down()
move_box()
up_and_down()
move_box()
up_and_down()

# While Loop
while condition_is_true:
   # Do this

# Final Challenge for Day 6
while front_is_clear:
   move()

turn_left()

while not at_goal():
   if right_is_clear():
      turn_right()
      move()
   elif front_is_clear():
      move()
   else:
      turn_left()