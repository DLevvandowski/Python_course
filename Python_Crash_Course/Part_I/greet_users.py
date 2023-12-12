# Very often it will be useful to pass a list to a function, for example, names, numbers or more complex objects such as
# dictionaries. When there is a need to pass a list to a function, then that function gets direct access to the contents
# of the list in question. We will now use functions to work with lists much more efficiently.

def greet_users(names):
    """Displays greetings every user from the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)


usernames = ['dave', 'mike', 'tom']
greet_users(usernames)
