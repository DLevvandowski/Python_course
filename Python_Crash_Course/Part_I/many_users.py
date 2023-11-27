# You can nest a dictionary within another dictionary, but in that case the code very quickly becomes quite complicated.
# For example, if a website will be used by many users with unique names, the names of these users can be used as
# dictionary keys.

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton'
        },
    'mcurie': {
        'first': 'maria',
        'last': 'sklodowska-curie',
        'location': 'paris'
        },
    }

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tName: {full_name.title()}"
          f"\n\tCity: {location.title()}")
