from sys import argv # Imports argv function from the sys module

script, filename = argv # unpacks 2 variables into argv function. First is the script name, second will be used for the filename

txt = open(filename) # Sets the opening of the file to a variable 'txt'

print(f"Here's your file {filename}:") # prints the intro
print(txt.read()) # Prints the content of the file

print("Type the filename again:") # Prints a prompt to the user (without the prompt itself)
file_again=input("> ") # Displays a prompt to receive input from the user, set to 'file_again' variable

txt_again = open(file_again) # Sets the opening of the file to a variable

print(txt_again.read()) # Prints the content of the second filename specified by the user above