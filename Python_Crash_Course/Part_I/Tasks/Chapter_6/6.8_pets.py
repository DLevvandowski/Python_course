# Ex. 6.8 Pets
# Create several vocabularies and give them animal names. In each dictionary, put information about the animals that own
# them. Then these dictionaries should be in a list named pets. Now iterate through the list and display all the
# information about each animal.

dog = {
    'type': 'dog',
    'name': 'lucifer',
    'breed': 'yorkshire terrier',
    'owner': 'damian lewandowski',
    'city': 'cracow',
    }

cat = {
    'type': 'cat',
    'name': 'garfield',
    'breed': 'sofa cat',
    'owner': 'monica lewandowska',
    'city': 'janow',
    }

hamster = {
    'type': 'hamster',
    'name': 'jacob',
    'breed': '---',
    'owner': 'juliet lewandowska',
    'city': 'zwolen',
    }

pets = [dog, cat, hamster]

for pet in pets:
    print(f"Type: {pet['type'].title()}\n"
          f"\tName: {pet['name'].title()}\n"
          f"\tBreed: {pet['breed'].title()}\n"
          f"\tOwner: {pet['owner'].title()}\n"
          f"\tCity: {pet['city'].title()}\n"
          f"-----")
