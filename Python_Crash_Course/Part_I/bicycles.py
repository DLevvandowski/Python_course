# The way to declare a list in a variable
bicycles = ['trekking', 'mountain', 'city', 'road']

# Displaying the list
print(bicycles)

# Displaying a list item
print(bicycles[0])

# We can use string methods on list items. The following example will display the element in uppercase.
print(bicycles[0].title())

# The first element of the list is at position 0, not 1.
# In the following example, we retrieve list elements with indexes 1 and 3, so we display the second and fourth element.
print(bicycles[1])
print(bicycles[3])

# Access the last element in the list
print(bicycles[-1])

# In the following code snippet, we retrieve the first bike from the list,
# and then we create a message containing this value.
message = f"My first bike was a {bicycles[0].title()} bike."
print(message)
