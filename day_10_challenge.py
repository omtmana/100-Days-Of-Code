#  Create a calculator

total = 0
is_calculating = False


def calculate_nums(n1, n2, sign):
  if sign == "+":
    return n1 + n2
  elif sign == "-":
    return n1 - n2
  elif sign == "*":
    return n1 * n2
  elif sign == "/":
    return n1 / n2


while not is_calculating:
  num_1 = int(input("What's your first number? "))
  print("+")
  print("-")
  print("*")
  print("/")
  operator = str(input("Choose an operation: "))
  num_2 = int(input("What's your second number? "))
  total = calculate_nums(n1=num_1, n2=num_2, sign=operator)
  print(f"{num_1} {operator} {num_2} = {total}")
  should_continue = input(
      str(f"Do you want to calculate from {total}? Type 'y' or 'n' to exit: "))
  if should_continue == "n":
    is_calculating == True
  elif should_continue == "y":
    num_1 = total
   