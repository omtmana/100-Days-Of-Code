# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇
print("My Tip Calculator")
bill = int(input("What is the total bill? "))
people = int(input("How many people are there? "))
tip = float(input("What tip percantage do you want to give? 10, 12, or 15? "))

total_tip = (tip / 100) + 1
bill_with_tip = round((bill * total_tip) + bill, 2)

payment_per_person = round(bill_with_tip / people, 2)