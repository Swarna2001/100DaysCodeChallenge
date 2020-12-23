# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# Converting the age variable from 'str' to 'int'
age = int(age)

# The maximum age limit given in the question is 90.
# So the number of years we left can be calculated.
remaining_years = 90 - age

# Given 1 year = 365 days = 52 weeks = 12 months

# Calculating the remaining_years in terms of days
remaining_days = remaining_years * 365

# Calculating the remaining_years in terms of weeks
remaining_weeks = remaining_years * 52

# Calculating the remaining_years in terms of months
remaining_months = remaining_years * 12

# Display the appropriate message
message = f"You have {remaining_days} days, {remaining_weeks} weeks, and {remaining_months} months left."
print(message)










