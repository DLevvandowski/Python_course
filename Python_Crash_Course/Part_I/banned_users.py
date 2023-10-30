# Checking if the value is not in the list
# Sometimes it is essential to check whether a value does not appear in the list. In such a situation, the keyword not
# comes to your aid. Consider, for example, a list of users who are banned from posting comments on the forum.

banned_users = ['andrew', 'caroline', 'david']
user = 'maria'

if user not in banned_users:
    print(f"{user.title()}, you can text something, if you want.")
