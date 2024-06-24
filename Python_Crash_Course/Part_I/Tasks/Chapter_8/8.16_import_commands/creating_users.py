def create_profile(first, nickname, email, age, **user_info):
    """Building a dictionary containing all user information."""
    user_info['nickname'] = nickname
    user_info['first_name'] = first
    user_info['email'] = email
    user_info['age'] = age
    return user_info

