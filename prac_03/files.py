"""
CP1404/CP5632 Practical
Make the appropriate choice of file-reading technique for each of these questions:
- read()
- readline()
- readlines()
- for line in file
"""

# 1
FILENAME = "name.txt"
out_file = open(FILENAME, 'w')
name = input("What is your name? ")
print(name, file=out_file)
out_file.close()

# 2
in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()
print(f"Hello, {name}!")