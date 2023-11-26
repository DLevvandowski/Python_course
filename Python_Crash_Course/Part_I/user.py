# Based on the knowledge you have gained so far in this chapter, you are able to access a single piece of information
# about a user whose data is in the user_0 dictionary. What can you do in a situation where you want to retrieve all the
# information about a particular user from the dictionary? To do this, you can use a for loop to iterate through the
# dictionary.

user_0 = {
    'username': 'dlewandowski',
    'first': 'damian',
    'last': 'lewandowski',
    }

for key, value in user_0.items():
    print(f"\nKey: {key}; Value: {value}.")
