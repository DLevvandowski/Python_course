# Slice
# It is possible to work with a specific group of list elements, which Python refers to as a slice.
# To create a slice, specify the index of the first and last elements, that you want to work with.
# To create a slice containing the first three elements of the list, you need to use a starting index of 0 and a final
# index of 3, which will result in the return elements with indexes 0, 1 and 2.

players = ['karol', 'martyna', 'michael', 'florian', 'ela']
print(players[0:3], '\n')

# It is possible to generate any subset of the list. If, for example you want to get the second, third and fourth
# elements of the list, then when defining the slice you must specify a starting index of 1 and an ending index of 4.

print(players[1:4], '\n')

# If you skip the initial index, Python automatically starts the clipping from the beginning of the list.

print(players[:4], '\n')

# For example, if you want to get a slice containing elements from the third to the end, then specify 2 as
# the initial index and skip the last index.

print(players[2:], '\n')

# With a negative index value, you can create any slice from the end of the list.
# For example, if you want a slice containing the last three elements of the list, specify -3 as the initial index,
# as I have shown in the code snippet below.

print(players[-3:], '\n')

# Iteration through the slice
# The slice can be used in a for loop if you need to iterate through a subset of list elements.
# In the following example, we iterate through the first three elements and display
# the players names in a simple sentence.

print('There are the first three players of our team: ')
for player in players[:3]:
    print(player.title())
