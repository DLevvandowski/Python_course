# Ex. 8.13 User profile
# Start your work with a copy of the user_profile.py program created a little earlier in this chapter. Prepare your own
# profile by calling the build_profile() function, provide a first name, last name and three other key-value pairs that
# describe you.

def build_profile(first, last, current_job, age, sex, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    user_info['current_job'] = current_job
    user_info['age'] = age
    user_info['sex'] = sex
    return user_info


user_profile = build_profile('albert', 'einstein', 'Salesman', 29, 'Male')
print(user_profile)
