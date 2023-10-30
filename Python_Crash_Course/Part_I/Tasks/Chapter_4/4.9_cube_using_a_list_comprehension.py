# Ex. 4.9 Cube using a list comprehension
# Use the folding list to generate a list of the first ten cubes. Display the list using for loop.

cubes = [value ** 3 for value in range(1, 11)]

for cube in cubes:
    print(cube)
