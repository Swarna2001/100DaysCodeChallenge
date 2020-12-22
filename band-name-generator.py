#1. Create a greeting for your program.
print("Hola ! Welcome to Band Name Generator Project.")
print("This project will help you to find an amazing band name, unique for you in few simple steps.")

#2. Ask the user for the city that they grew up in.
user_city = input("\nEnter the name of the city you were brought up in :\n")

#3. Ask the user for the name of a pet.
user_pet = input("\nEnter the name of the pet that you have :\n")

#4. Combine the name of their city and pet and show them their band name.
band_name = user_city + "_" + user_pet
print("\nA possible brand name you can have is " + band_name)

#5. Make sure the input cursor shows on a new line, see the example at:
#   https://band-name-generator-end.appbrewery.repl.run/