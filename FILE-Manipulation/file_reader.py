# Creating the list of the lines

filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''

# We using .strip() instead of .rstrip() to remove all white marks
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))
