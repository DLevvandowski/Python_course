# Consider a game in which there are aliens of different colors, and the number of points obtained after shooting down
# an alien depends on its color. Below I have presented a dictionary designed to store information about the aliens.

alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

# The simplest dictionary has exactly one key-value pair, as I have shown below in a new alien_1 dictionary.

alien_1 = {'color': 'blue'}

# This dictionary stores one piece of information about the alien, specifically its color. In the discussed dictionary,
# the text string 'color' is the key with which the value 'green' is associated.
# Now you can access the color of the alien and the number of points awarded for shooting it down. If a player shoots
# down an alien, the number of points to be awarded to it can be checked using a code similar to the following.

print('-----')
new_points = alien_0['points']
print(f"You've earned {new_points} points!")

# The dictionary is a dynamic structure, so new key-value pairs can be added at any time. To add a new key-value pair,
# specify the name of the dictionary, the name of the new key enclosed in square brackets, and the value assigned to the
# key.

print('-----')
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# Sometimes it will be convenient or even necessary to start with an empty dictionary, into which only later key-value
# pairs will be inserted. To start filling an empty dictionary, define it with an empty curly bracket, and then add
# individual key-value pairs, one in each row.

print('-----')
alien_2 = {}

alien_2['color'] = 'red'
alien_2['points'] = 10
print(alien_2)

# To modify a value in a dictionary, specify the dictionary name, the key name enclosed in square brackets, and the new
# value to be assigned to the indicated key.

print('-----')
print(f"Alien number 2 is {alien_1['color']}.")

alien_1['color'] = 'yellow'

print(f"Alien number 2 is {alien_1['color']} now.")

# A more interesting example might be monitoring the position of a alien that moves at different speeds. We store a
# value in the dictionary that specifies the current speed of the alien and use it to determine the distance the alien
# moving to the right should travel.

print('-----')
alien_3 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Basic value of x_position: {alien_3['x_position']}")

if alien_3['speed'] == 'slow':
    x_increment = 1
elif alien_3['speed'] == 'medium':
    x_increment = 2
else:
    # It must be a fast alien.
    x_increment = 3

alien_3['x_position'] = alien_3['x_position'] + x_increment

print(f"New value of x_position: {alien_3['x_position']}")

# When a piece of information stored in the dictionary is no longer needed, the del command can be used to completely
# remove the key-value pair. To work properly, the del command needs to have the dictionary name and the key to be
# deleted specified.

print('-----')

alien_4 = {'points': 10, 'color': 'brown'}

print(f'Alien number five: {alien_4}')

del alien_4['points']

print(f'New Alien number five: {alien_4}')

# Note that the operation of deleting a key-value pair is irreversible.
