# Ex. 6.9 Favorite places
# Create a dictionary named favorite_places. Think of three names and use them as dictionary keys. Assign three favorite
# places to each person. To make the exercise even more interesting, you can ask your friends to name their favorite
# places. Iterate through the dictionary and display everyone's names and their favorite places.

favorite_places = {
    'damian': ['sofa', 'mountains', 'sea'],
    'claudia': ['sea', 'italian restaurant', 'bed'],
    'juliet': ['main square', 'club', 'home'],
    }

for person, places in favorite_places.items():
    print(f"\n{person.title()}'s favorite places:")
    for place in places:
        print(f"\t{place.title()}")