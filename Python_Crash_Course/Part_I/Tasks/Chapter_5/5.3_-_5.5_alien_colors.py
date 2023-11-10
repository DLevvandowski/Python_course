# Ex. 5.3 Alien colors, part I
# Imagine shooting down an alien in the game. Create a variable named alien_color and assign it the value 'green',
# 'yellow' or 'red'.
#  Prepare an if command to check if the alien's color is green. If it is, display a message informing the player that
#   he has earned five points.
#  Prepare a version of the program that passes the above test and another that fails. (The failing version should not
#   generate any output).

print("Ex. 5.3")
print("Passes test:")
alien_color = 'green'

if alien_color == 'green':
    print("You score 5 points!")

print("\nFails test:")
alien_color = 'red'

if alien_color == 'green':
    print("You score 5 points!")

print("\n-----\n")
# Ex. 5.4 Alien colors, part II
# As in exercise 5.3, choose a color for the alien, and then create an if-else construct.
#  If the color of the alien is green, display a message informing the player, that he has earned five points for
#   shooting down this alien.
#  If the color of the alien is other than green, display a message informing the player that he has earned ten points
#   for shooting down this alien.
#  Prepare a version of the program that executes the if block and another that executes the else block.

print("Ex. 5.4")

print("Executing else block:")
alien_color = 'yellow'

if alien_color == 'green':
    points = 5
else:
    points = 10

print(f"You score {points} points!")

print("\nExecuting if block:")
alien_color = 'green'

if alien_color == 'green':
    points = 5
else:
    points = 10

print(f"You score {points} points!")

print("\n-----\n")

# Ex. 5.5 Alien colors, part III
# The construction prepared in exercise 5.4 if-else replace the if-elif-else construction.
#  If the color of the alien is green, display a message informing the player, that he has earned five points for
#   shooting down this alien.
#  If the color of the alien is yellow, display a message informing the player that he has earned ten points for
#   shooting down this alien.
#  If the color of the alien is red, display a message informing the player, that he has earned fifteen points for
#   shooting down this alien.
#  Prepare three versions of the program and make sure that each message is displayed for the corresponding color of
#   the alien shot down.

print("Ex. 5.5")

print("Executing if block:")
alien_color = 'green'

if alien_color == 'green':
    points = 5
elif alien_color == 'yellow':
    points = 10
else:
    points = 15

print(f"You score {points} points!")

print("\nExecuting elif block:")
alien_color = 'yellow'

if alien_color == 'green':
    points = 5
elif alien_color == 'yellow':
    points = 10
else:
    points = 15

print(f"You score {points} points!")

print("\nExecuting else block:")
alien_color = 'red'

if alien_color == 'green':
    points = 5
elif alien_color == 'yellow':
    points = 10
else:
    points = 15

print(f"You score {points} points!")
