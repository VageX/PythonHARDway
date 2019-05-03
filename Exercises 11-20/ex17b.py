from sys import argv
from os.path import exists
script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

indata = open(from_file).read()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()