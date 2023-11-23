# Ex. 5.10 Checking usernames
# Follow the steps below to create a program that simulates how a website guarantees that each user will have a unique
# name.
# » Create a list named current_users and put at least five usernames on it.
# » Create another list named new_users. Make sure that at least one username from the new list is also in the
#   current_users list.
# » Run an iteration through the new list to see if the username has been used before. If so, display a message to the
#   user to select another name. On the other hand, if the username has not been used before, display a message to the
#   user indicating that it can be used.
# » Make sure that the username is not case-sensitive when comparing usernames. If the name 'Jan' has been used before,
#   the new user cannot choose the name 'JAN' for himself. (This requires creating a copy of the current_users list
#   containing the lowercase names of all users).

current_users = ['coco', 'Jumbo', 'mAxi_tom', 'MyName', 'BaNaNaBoY']

new_users = ['bAnAnAbOy', 'BlueCuracao', 'tomas', 'ProGamer', 'g0d']

lower_current_users = []

for user in current_users:
    lower_current_users.append(user.lower())

if new_users:
    if lower_current_users:
        for user in new_users:
            if user.lower() in lower_current_users:
                print(f'\nUsername {user} is taken. Choose another one.')
            else:
                print(f'\nYou can use {user} as your username.')
    else:
        for user in new_users:
            print(f'\nYou can use {user} as your username.')
else:
    print("Are you sure you don't want to use any username?")
