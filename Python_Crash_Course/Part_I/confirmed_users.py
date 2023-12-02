# Consider a list of newly registered website users who have not yet been verified. Once the user has been verified,
# move the user to the list of confirmed users.

unconfirmed_users = ['alice', 'bart', 'kate']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"User verification: {current_user.title()}.")
    confirmed_users.append(current_user)

print("\nThe users listed below have been verified:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
