from sys import argv

script, input_file = argv

def print_all(f):
    '''Prints a file's content'''
    print(f.read())

def rewind(f):
    '''Resets file handle to index 0 (the beginning)'''
    f.seek(0)

def print_a_line(line_count, f):
    '''Prints the current line count and line of text'''
    print(line_count, f.readline(), end="")

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

# Each line is printed by increasing 'current_line' after each successive line
current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)