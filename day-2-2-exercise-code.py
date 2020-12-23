# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# Converting the 'str' types to 'float' types
height = float(height)
weight = float(weight)

# Calculating BMI Index as per the formula BMI INDEX = (WEIGHT) / ( (HEIGHT) * (HEIGHT) )
bmi_index = weight / (height ** 2)

# Converting the floating value to an integer in the bmi_index variable.
bmi_index = int(bmi_index)

# Printing the BMI index calculated
print(bmi_index)










