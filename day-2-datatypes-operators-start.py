# Data Types

# Strings - a sequence of characters enclosed within double or single quotes

# The characters that make up a string object can be accessed
# using the [] operator. Within the [], specify the index position where 
# the required character is present.
name = "Swarna"
print(name[0])  # prints the character S

# If you want to access a sequence of characters, specify the start and ending
# position using the : operator within []. NOTE THAT THE SEQUENCE OBTAINED WOULD
# NOT INCLUDE THE CHARACTER AT END POSITION.
print(name[1:4]) # prints the output war

# Strings are immutable objects after definition
# The below example throws the TypeError as 'str' object doesnot support item assignment.
name = "Swarna"
# name[3] = 't'   

# Integers can be represented by simply declaring them.
age = 23
print(age)

# Floating point numbers come under the float datatype. 
price = 245.567

# Boolean datatype has two values - True / False
print(2 == 3)

# The type() function is used to find out what is the data type
# that a variable corresponds to. You can also use type casting,
# a process to convert a variable from one datatype to another.

old_num_char = len(input("What is your name ?\n"))

print(type(old_num_char))

new_num_char = str(old_num_char)

print(type(new_num_char))

# This statement is wrong because the old_num_char is an integer and not a string.
# print("Your name has " + old_num_char + " characters")

# Correct statement
print("Your name has " + new_num_char + " characters")

# Operators

# Addition        (+)     3 + 5
# Subtraction     (-)     9 - 7
# Multiplication  (*)     3 * 4
# Division        (/)     6 / 3     ---> THIS RETURNS A FLOATING VALUES
# Division        (//)    7 // 2    ---> THIS RETURNS AN INTEGER VALUES
# Exponentation   (**)    2 ** 3    ---> 2 raised to the power of 3

# The operators have priority assigned to them
# (), **, * / (left-to-right), + - (left-to-right)

# If you want to round numbers, you can use the round function.
# Apart from the variable name, you can also specify the number of 
# digits you would like to round to.

price = 8 / 3
round_price = round(price)
round_price_with_2_digits = round(price, 2)
print(price, round_price, round_price_with_2_digits)

# F Strings - You use them when you don't want to keep
# worrying about converting data when concatenating them.
score = 0
money = 245.67
# Instaed of the below cumbersome stt, we use f strings.
# print("Your score is " + str(score) + "\nYour money is " + str(money))
print(f"Your score is {score}\nYour money is {money}")
