# The function does not always have to directly display the generated data. Instead, it can process some data and return
# a value or set of values. This type of value returned by a function is referred to as a return value. The return
# statement takes a value from within a function and passes it to the line of code where the function was called. With a
# return value, most of the tasks performed by a program can be transferred to a function, which greatly simplifies the
# main part of the application.The function does not always have to directly display the generated data. Instead, it can
# process some data and return a value or set of values. This type of value returned by a function is referred to as a
# return value. The return statement takes a value from within a function and passes it to the line of code where the
# function was called. With a return value, most of the tasks performed by a program can be transferred to a function,
# which greatly simplifies the main part of the application.

def get_formatted_name(first_name, last_name):
    """Returns an elegantly formatted full name."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musican = get_formatted_name('adam', 'gontier')
print(musican)

# To make the second name optional, the middle_name argument must be assigned a default value in the form of an empty
# text string and ignored if the user does not provide a value for the listed argument.

print('-----')
def get_formatted_name(first_name, last_name, middle_name = ''):
    if middle_name:
        full_name = f'{first_name} {middle_name} {last_name}'
    else:
        full_name = f'{first_name} {last_name}'
    return full_name.title()

musican = get_formatted_name('adam', 'gontier')
character = get_formatted_name('tom', 'riddle', 'marvolo')

print(musican)
print(character)
