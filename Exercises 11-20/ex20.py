from sys import argv

script, input_file = argv
# Create a function to read the inputted file in format.
def print_all(f):
    print(f.read())
# Create a function to set the file's position at zero
def rewind(f):
    f.seek(0)
# Create a function to label the current line in numerical order and read it.
def print_a_line(line_count, f):
    print(line_count, f.readline())
# Open the inputted file and name it as the current file
current_file = open(input_file)

print("First let's print the whole file:\n")
# Call the print_all function to read the entire current file.
print_all(current_file)

print("Now let's rewind, kind of like a tape.")
# Call the rewind function to set the current file's position at zero.
rewind(current_file)

print("Let's print three lines:")
# Begin at line 1
current_line = 1

print_a_line(current_line, current_file)
# Move on to the next line (2)
current_line = current_line + 1
print_a_line(current_line, current_file)
# Move on to the next line (3)
current_line = current_line + 1
print_a_line(current_line, current_file)