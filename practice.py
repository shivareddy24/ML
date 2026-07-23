filename = input("Enter the file name: ")

with open(filename, "r") as file:
    lines = file.readlines()

line_count = len(lines)
word_count = sum(len(line.split()) for line in lines)

print("Lines:", line_count)
print("Words:", word_count)