# Ex. 4.7 Three
# Create a list of numbers from 3 to 30 raised to the third power, and then display the contents of the list.
# Use a for loop.

values = []

for value in range(3, 31):
    raised_value = value ** 3
    values.append(raised_value)

for value in values:
    print(value)
