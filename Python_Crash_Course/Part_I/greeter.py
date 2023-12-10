# Whenever you use the input() function, you should try to prepare a clear and understandable message that explains to
# the user exactly what kind of information is expected. Here, any message indicating to the user what information he
# should provide will work. Look at the example shown below.

name = input("Enter your name: ")
print(f"Hello, {name.title()}!")

# Sometimes you need to prepare a message much longer than just one line of text. For example, in a message you explain
# to the user exactly why you are asking for specific information. In this case, you can put the message in a variable,
# which will then be passed to the input() function. In this way, you can prepare a really long message, followed by a
# clear and concise call to the input() function, as I have shown below.

print('-----')
prompt = "If you tell us who you are, we will personalize the displayed message."
prompt += "\nWhat's your name? "

name = input(prompt)
print(f"Hello, {name.title()}!")

# Below I've presented a simple function called greet_user(), whose task is to display a greeting.

print('-----')
def greet_user():
    """Displays a simple greeting."""
    print("Hello!")

greet_user()

# When a slight modification is made, the greet_user() function can not only display the word Hello!, but also the
# user's name. To do this, in the brackets of the function definition (def greet_user():) you need to enter the name of
# a variable, such as username. Adding the mentioned variable means that the function will accept any entered username
# value. After this change, the function expects a value for username every time it is called. Therefore, when calling
# the greet_user() function, you can pass the user's name to it in parentheses, for example 'jacob'

print('-----')
def greet_user(username):
    """Displays a simple greeting using a username"""
    print(f"Hello, {username.title()}!")

greet_user('jacob')

# You can use the function together with all Python structures you have learned so far. For example, we will use the
# get_formatted_name() function presented earlier with a while loop to greet users more formally.

def get_formatted_name(first_name, last_name):
    """Returns an elegantly formatted full name."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


while True:
    print("\n Please enter first and last name: ")
    print("(type 'q' to quit at any time)")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"Hello, {formatted_name}!")
