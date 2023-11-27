# One solution is to create a list of aliens, where each alien will be represented by a dictionary containing
# information about it. For example, in the code shown below, we have a list regarding three aliens.

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# A much more real-world example involves creating more than just three aliens using code that will automatically
# generate them.

print('-----')
aliens = []

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)
print('-----')

print(f"\nTotal number of aliens: {len(aliens)}")

# How can you work with this kind of collection of aliens? Imagine that one aspect of the game is to change the color of
# the alien and its speed with the progress made by the player.

print('-----')
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['points'] = 15
        alien['speed'] = 'fast'

for alien in aliens[:5]:
    print(alien)
print('-----')
