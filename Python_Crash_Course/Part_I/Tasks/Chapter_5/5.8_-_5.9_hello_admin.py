# Ex. 5.8 Hello, admin!
# Prepare a list of at least five usernames, including, but not limited to, the name 'admin'. Imagine that you are
# creating code responsible for greeting a user when he or she logs into the website. Iterate through the loop and
# display the greeting for each user.
# » If the username is 'admin', display a special greeting in the style of:
#   "Hello, admin! Would you like to review today's report?".
# » For other users, display a simple greeting like:
#   "Hello, Eric! Thank you for logging in again."

user_list = ['coco', 'admin', 'theboywholived', 'tom', 'jumbo']

if user_list:
    for user in user_list:
        if user == 'admin':
            print(f"Hello, {user}! Would you like to review today's report?")
        else:
            print(f"Hello, {user}! Thank you for logging in again.")
else:
    print("Lack of users.")

print('-----')
# Ex. 5.9 Lack of users
# Add an if command to the hello_admin.py file prepared in the previous exercise to check if the list of users is empty.
# » If the list is empty, display a message like: "We need to find some users!".
# » Remove all users from the list and make sure the above message is displayed correctly.

user_list = []

if user_list:
    for user in user_list:
        if user == 'admin':
            print(f"Hello, {user}! Would you like to review today's report?")
        else:
            print(f"Hello, {user}! Thank you for logging in again.")
else:
    print("We need to find some users!")
