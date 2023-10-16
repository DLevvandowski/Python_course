# The range() function makes it easy to generate a series of numbers.
# For example, using it, you can generate a series of numbers in the manner shown below.

for value in range(1,6):
    print(value)
print('---')
# The range() function can be passed only one argument, in which case the sequence of of numbers will start from 0.

for value in range(6):
    print(value)
print('---')

# If you want to create a list of numbers, the result of calling range() can be directly convert it to a list
# using the list() function. If you want to create a list of numbers, the result of calling range() can
# be directly convert to a list using the list() function.

numbers = list(range(1,6))
print(numbers)
print('---')