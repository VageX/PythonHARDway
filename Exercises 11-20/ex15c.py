# prompt the filename again to be read.
print("Type the file name: ")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

txt_again.close()