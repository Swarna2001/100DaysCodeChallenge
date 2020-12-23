# The objective of this program is to simulate a tip calculator.
# The program will ask the user to input the total bill amount, percentage of tip,
# and the number of peple to divide. Based on the given values, the program
# calculates the amunt each person has to pay.

#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

# Greeting the user
print("Hello there ! Welcome to the tip calculator.")

# Prompting the user for the total bill amount
bill_amount = float(input("Enter the total bill amount (in $): "))

# Prompting the user for tip amount (measured in %)
tip_percentage = float(input("Enter the tip (in percentage) : "))

# Prompting the user for the number of people 
number_of_people = int(input("Enter the number of people for the bill split : "))

# Calculate the actual amount to be paid - add the tip amount
total_amount = bill_amount * (1 + tip_percentage / 100)

# Calculate the amount to be paid by a single person
amount_per_individual = total_amount / number_of_people

# Round the amount_per_individual to 2 decimal places.
amount_per_individual = round(amount_per_individual, 2)

# Display the amount to the user
print(f"The amount to be paid by a single member is {amount_per_individual}")