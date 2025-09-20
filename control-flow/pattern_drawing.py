# pattern_drawing.py


# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter for while loop
row = 0

# Outer loop (controls rows)
while row < size:
    # Inner loop (controls columns)
    for col in range(size):
        print("*", end="")  # print star without new line
    print()  # move to the next line after each row
    row += 1
