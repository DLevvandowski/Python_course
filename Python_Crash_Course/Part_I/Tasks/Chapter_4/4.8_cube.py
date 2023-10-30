# Ex. 4.8 Cube
# A number raised to the third power is called a cube. For example, the cube of the number 2 is written in Python
# as 2**3. Create a list of the first ten cubes (that is, numbers from 1 to 10 raised to the third power),
# and then display them using a for loop.

cubes = []

for value in range(1, 11):
    cube = value ** 3
    cubes.append(cube)

for cube in cubes:
    print(cube)
