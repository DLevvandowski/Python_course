# Ex. 4.13 Buffet
# The buffet-style restaurant offers only five simple dishes. So list the five simple dishes and put them in a tuple.
#  Using a for loop, display all the dishes offered by the restaurant.
#  The restaurant changes the menu and replaces two existing dishes with new ones.
# Add a block of code that overwrites the tuple, and then use the for loop to display all the dishes
# from the modified menu.

buffet = ('scrambled eggs', 'cereals', 'pancakes', 'sausages', 'bread')

print('Menu of buffet: ')
for food in buffet:
    print(food)

buffet = ('scrambled eggs', 'cereals', 'pancakes', 'cream cheese', 'milk')

print('\nModified menu of buffet: ')
for food in buffet:
    print(food)
