# We assume that we have a list of magicians names, and we want to display them all.
# We will use a for loop to display the names of all the magicians included in the list.

magicians = ['alicja', 'dawid', 'karolina']
for magician in magicians:
    print(magician)

print('---')

# Now we will expand the previous example to add a message for each magician,
# including a thank you for performing a great trick.

for magician in magicians:
    print(f'{magician.title()}, that was a great trick!')

print('---')

# We will now add a second line to the generated message informing the magician about
# how we are looking forward to his next show.

for magician in magicians:
    print(f'{magician.title()}, that was a great trick!')
    print(f'I look forward to your next trick, {magician.title()}.\n')

print('---')

# We will now create a message for the group of magicians as a whole,
# in which we will thank them for their excellent performance.

for magician in magicians:
    print(f'{magician.title()}, that was a great trick!')
    print(f'I look forward to your next trick, {magician.title()}.\n')

print('Thank you all. It was really a great show!')

print('---')