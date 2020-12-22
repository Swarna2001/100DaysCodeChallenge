# A simple command to print a string of characters is the 
# print statement. The text to be printed is enclosed in double 
# quotes within the parentheses.
print("Hello World !")

# In order to print a string multiple amount of times by using
# a single print command, we can specify the text with the help
# of the \n sequence.

print("Hello World !\nHello World !\nHello World !")

# The '+' operator can be used as a simple way of concatenating
# multiple strings together as a single open

# Note that there is no space between the words when you print
# them on the screen. This is because the '+' operator blindly
# concatenates the given strings. It doesn't add anything.
print("Hello" + "Swarna") 

# If you want to provide a space between the words, you can
# write either of the following statements.
print("Hello " + "Swarna")
print("Hello" + " " + "Swarna")
print("Hello" + " Swarna")

# input() function is used to prompt the user of data and get it
# input(prompt) is the basic syntax, where the word 'prompt' refers to the the sentence to be displayed when we ask the user for the data

input("What is your name ?")

# When you run the above function, in the output screen, you will
# have the propmt displayed waiting for some input to be entered.
# After you enter an input and hit Enter, the above line of code
# gets replaced entirely with the data you entered.
# input("What is your name ? ") <--- Swarna
# You can use the output of the input statement inside other code. 

print("Hello " + input("What is your name ? "))
# In the above piece of code, first the input() command is 
# executed. The data entered as part of its execution replaces it
# in the above statement. It is then concatenated by the "+"
# operator and passed to the print() function to be printed.

# The len() function is used to print the number of characters 
# in the container passed to it. So here, in the below example,
# the answer we would get would be 6.
print(len("Angela"))
