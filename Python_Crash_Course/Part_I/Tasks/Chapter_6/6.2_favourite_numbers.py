# Ex. 6.2 Favourite numbers
# Use the dictionary to store favorite numbers of different people. Consider five people and use their names as
# dictionary keys. Then determine their favorite numbers and put them in the dictionary, assigning one number to each
# person. Display the names of all the people and their favorite numbers. If you want to have more fun while doing this
# exercise, ask your friends about their favorite numbers and put the actual data in the program.

favourite_numbers = {
    'john': 5,
    'sarah': 12,
    'david': 21,
    'claudia': 7,
    'damian': 11,
    }

print(f"John favourite number is {favourite_numbers['john']}. Sarah favourite number is {favourite_numbers['sarah']}."
      f" David favourite number is {favourite_numbers['david']}. Claudia favourite number is "
      f"{favourite_numbers['claudia']}. Damian favourite number is {favourite_numbers['damian']}.")
