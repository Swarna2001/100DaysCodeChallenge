# The below function helps us to get some data from the user. But this data cannot be re used
# again in other parts of the code. This is because, the machine will not be able to identify
# and find out which memory location corresponds to our data - bcoz no name was given to it.
input("What is your name?")

# To access and stre data for further uses, we make use of "variable". A variable is a name
# that we assign to access and modify data. It can be used wherever we want and any types of
# data can be stored in it. 

name = input("What is your name?")
print(name)

# In the above example, we will overcome the problem we faced earlier. The machine will now
# know what data we want, and will be able to retrieve it for us. It is also possible for 
# us to change this data to a new one in a simple way like below code.

name = "Jack"
print(name)

name = "Angela"
print(name)

# For naming your variables, there are some rules to be followed.

# 1. Name variables such that your code becomes more readable.

n = "Jake"      # WRONG NAMING - VERY LESS READABLE
name = "Jake"   # CORRECT NAMING - MUCH MORE READABLE THAN PREVIOUS ONE

# 2. If you want to use multiple words in a single name, then specify it with _ as their separator.

user_name = "Drew"  # DO NOT USE A SPACE TO SEPARATE THE WORDS - INVALID CODE

# 3. You can use numbers in your variable names. But they cannot be used as the starting character.
# 123Name = "JK" - WRONG NAMING   Name123 = "JK" - CORRECT NAMING

# 4. There are certain words that are used and reserved as keywords - meaning that they have special purpose.
# So DO NOT USE SUCH NAMES AS THE NAMES FOR YOUR VARIABLES.

# 5. If you use variables that haven't been initialised or defined, you will thrown a "NameError".