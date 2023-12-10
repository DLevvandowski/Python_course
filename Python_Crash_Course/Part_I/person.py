# The return value of the function can be of any type, including the inclusion of more complex data structures, such as
# a list or dictionary, for example.

def build_person(first_name, last_name):
    """Returns a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person

musican = build_person('adam', 'gontier')
print(musican)

# This function can be further extended to accept additional values, such as second name, age, locality and any other
# information we want to store about a person.

def build_person(first_name, last_name, age = None):
    """Returns a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musican = build_person('adam', 'gontier', age = 45)
print(musican)
