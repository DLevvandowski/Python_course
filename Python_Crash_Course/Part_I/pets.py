# We assume that there is a list of animals in which the element 'cat' repeatedly appears. To remove all occurrences of
# this value, we can use a while loop as long as the value 'cat' is in the list, as I have shown in the following
# program.

pets = ['dog', 'cat', 'dog', 'gold fish', 'cat', 'rabbit', 'hamster', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)