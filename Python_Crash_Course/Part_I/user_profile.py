# Sometimes it is necessary to accept any number od arguments, although beforehand it is not clear what kind of
# information will be passed to the function. In such a case, you can prepare functions that accept any number of
# key-value pairs provided by the command calling the function.

def build_profile(first, last, **user_info):
    """Building a dictionary containing all user information."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)
