# Ex. 4.10 Slices
# Start your work with one of the programs created in this chapter, and then at the end add a few lines of code
# performing the tasks listed below:
#  Display the message "The first three elements of the list are:". Then use the slice to display the first three
#   elements of the list.
#  Display the message "The three elements in the middle of the list are:". Then using the slice display
#   the three elements in the middle of the list.
#  Display the message "The last three elements in the list are:". Then using the slice display the last three
#   elements in the list.

cubes = [value ** 3 for value in range(1, 11)]

for cube in cubes:
    print(cube)

print('\n-----\n')
print("The first three elements of the list are: ")
print(cubes[0:3])

print('\n-----\n')
print("Three elements from middle of the list are: ")
print(cubes[3:6])

print('\n-----\n')
print("Last three elements of the list are: ")
print(cubes[-3:])
