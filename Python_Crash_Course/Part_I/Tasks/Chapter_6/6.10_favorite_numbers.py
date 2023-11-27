# Ex. 6.10 Favorite numbers
# Modify the program created in exercise 6.2 earlier in the chapter. After the changes, each person can have more than
# just one favorite number. Display all the people and their favorite numbers.

favourite_numbers = {
    'john': [5, 11, 23],
    'sarah': [12, 2],
    'david': [21, 53, 44, 5.5],
    'claudia': [7, 16, 29],
    'damian': [11, 16, 29, 15, 10],
    }

for person, numbers in favourite_numbers.items():
    print(f"\n{person.title()}'s favourite numbers:")
    for number in numbers:
        print(f"\t{number}")
