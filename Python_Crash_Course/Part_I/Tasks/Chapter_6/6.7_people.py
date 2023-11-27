# Ex. 6.7 People
# Start your work with the program created in Exercise 6.1 earlier in the chapter. Create two new dictionaries
# representing different people, and then put all three dictionaries into a list named people. Iterate through the list
# of people and display all the information about each person.

person_0 = {
    'first_name': 'damian',
    'last_name': 'lewandowski',
    'age': 28,
    'city': 'cracow',
    }

person_1 = {
    'first_name': 'claudia',
    'last_name': 'lewandowska',
    'age': 27,
    'city': 'cracow',
    }

person_2 = {
    'first_name': 'julita',
    'last_name': 'lewandowska',
    'age': 20,
    'city': 'cracow',
    }

people = [person_0, person_1, person_2]

for person in people:
    print(f"Name: {person['first_name'].title()} {person['last_name'].title()}\n"
          f"Age: {person['age']}\n"
          f"City: {person['city'].title()}\n"
          f"-----")
