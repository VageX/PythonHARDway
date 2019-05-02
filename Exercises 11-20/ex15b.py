# Import argument variable from the Python library.
from sys import argv

# Require filename argument to run program
script, filename = argv

# Open the file
txt = open(filename)

# Read the given file
print(f"Here's your file {filename}:")
print(txt.read())

# prompt the filename again to be read.
