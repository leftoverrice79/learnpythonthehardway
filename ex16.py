from sys import argv
script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do not want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for the three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")
print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# cr = "\n"
# writetxt = line1 + cr + line2 + cr + line3 + cr
# writetxt = f"{line1}{cr}{line2}{cr}{line3}{cr}"
# target.write(writetxt)

print("And finally, we close it.")
target.close()

# print("This is the contents of the modified file:")
# target = open(filename)
# print(target.read())

# target.close()