# Ex. 4.5 Adding up to a million
# Create a list of numbers from one to one million, and then using the min() and max() functions,
# check that the list actually starts begins with the value one and ends with one million.
# Also, use the sum() function, to see how quickly Python can add a million numbers.

values = list(range(1, 1000001))
print(min(values))
print(max(values))
print(sum(values))
