# You can use the range() function to create virtually any set of numbers.
# How can you create a list of the squares of the first ten numbers, that is, how to calculate the second power
# for integers from 1 to 10? In Python, the exponent is denoted by two asterisks (**).

squares = []

for value in range(1, 11):
    square = value**2
    squares.append(square)
print(squares)
print('---')

# The approach outlined above for generating a list of squares requires three or four lines of code.
# The so-called comprehension list allows you to generate exactly the same list, but with just one line of code.
# A comprehension list combines in a single line of code the loop for,
# the creation of a new element and its automatic inclusion in the list.

squares = [value**2 for value in range(1, 11)]
print(squares)
print('---')
