# In the previous example, we stored different types of information about a single object. However, the dictionary can
# also be used to store one type of information about multiple objects.

favourite_languages = {
    'john': 'python',
    'sarah': 'java',
    'edward': 'c++',
    'paul': 'python',
    }

language = favourite_languages['sarah'].title()
print(f"Sarah favourite programming language is {language}.")

# Since keys always refer to a person's name, and value always represents a programming language, so variables in a for
# loop can be named name and language instead of the generic key and value. This will make the purpose of the loop much
# easier to understand.

print('-----')
for name, language in favourite_languages.items():
    print(f"{name.title()} favourite language is {language.title()}.")

# The keys() method is useful when you don't need to process all the values in the dictionary. In the following code
# snippet, we iterate through the favorite_languages dictionary and display the names of all survey participants.

print('-----\n'
      'Survey participants: ')
for name in favourite_languages.keys():
    print(name.title())

# Inside the for loop, you can access the value associated with the key, which requires the use of the current key.
# A few friends will now be shown a message about their chosen programming languages. As we did before, we iterate
# through the names in the dictionary, but when we match a name to one of our friends, we display a message about his
# favorite programming language.

print('-----')
friends = ['paul', 'sarah']
for name in favourite_languages.keys():
    if name in friends:
        language = favourite_languages[name]
        print(f"Hello, {name.title()}! I see that your favorite programming language is {language.title()}!")
    else:
        print(f"Hello, {name.title()}")

# It is also possible to use the keys() method to find a specific person who took the survey. This time, we are checking
# if Elizabeth has taken the survey

print('-----')
if 'elizabeth' not in favourite_languages.keys():
    print("Elizabeth, please participate in our survey!")

# Starting with the Python 3.7 release, iterating through a dictionary always returns elements in the order in which
# they are inserted into the dictionary. However, sometimes there is a need to iterate in a completely different order.
# The only way to have the elements returned in the specified order is to sort the keys as they are received in the for
# loop. We can use the sorted() function to get ordered copies of the keys.

print('-----')
for name in sorted(favourite_languages.keys()):
    print(f"{name.title()} thank you for participating in the survey.")

# If we are primarily interested in the values stored in the dictionary, then the values() method can be used to return
# a list of values without any keys. For example, we assume that we want to retrieve a list of all programming languages
# listed by survey participants, and we are not interested in the names of the people indicating each language.

print('-----\n'
      'The following programming languages were mentioned in the survey:')
for language in favourite_languages.values():
    print(language.title())

# This kind of approach retrieves all values from the dictionary without checking if they repeat. To display only unique
# values, we can use a collection. The mentioned collection is similar to a list, but each element in it must be unique.

print('-----\n'
      'The following programming languages were mentioned in the survey:')
for language in set(favourite_languages.values()):
    print(language.title())

# You can create a collection directly using curly brackets, in which you need to place comma-separated elements:
# >>> languages = {'python', 'ruby', 'python', 'c'}
# >>> languages
# {'ruby', 'python', 'c'}
#
# It's very easy to confuse a collection with a dictionary, because in both cases a curly bracket is used. When you see
# curly brackets, but without key-value pairs, you are probably dealing with a collection. Unlike lists and dictionaries
# a collection does not store elements in any particular order.

favourite_languages = {
    'john': ['python', 'ruby'],
    'sarah': ['java'],
    'edward': ['c++', 'c#', 'c'],
    'paul': ['python', 'haskell'],
    }

for name, languages in favourite_languages.items():
    print(f"\nUser {name.title()}'s favourite programming languages are: ")
    for language in languages:
        print(f'\t{language.title()}')
