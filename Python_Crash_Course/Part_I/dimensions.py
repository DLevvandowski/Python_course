# Tuple
# Sometimes there is a need to create a list of elements that cannot change. This is where a tuple comes to the rescue.
# In Python, values that cannot change are referred to as unmodifiable, and an example of
# an unmodifiable list is a tuple.
# A tuple looks almost the same as a list, but uses round brackets instead of # square ones. After defining a tuple,
# access to its individual elements are accessed using an index, which is similar to a list.

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# Iterate through all the values of the tuple
# Iterating through all the values of the tuple can be done using a for loop, which is similar to a list.

print('-----')

for dimension in dimensions:
    print(dimension)

# Override tuple
# It is possible to assign a completely new value to the variable storing this tuple.
# Therefore, if we want to change the dimensions of the rectangle, we can redefine the entire tuple.
print('-----')

print('Dimensions before modification: ')
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)

print('\nDimensions after modification: ')
for dimension in dimensions:
    print(dimension)
