# Ex. 6.6 Survey
# Use the code found in favorite_languages.py, created a little earlier in this chapter.
# » Create a list of people who should participate in a survey about their favorite programming language. Put on it some
#   people who are already in the dictionary and those who are not yet in the dictionary.
# » Run an iteration through the list of people who should participate in the survey. If a person has already
#   participated in the survey, display a message thanking them for their involvement. On the other hand, if the person
#   has not yet responded to the survey, display a message inviting them to participate.

favourite_languages = {
    'john': 'python',
    'sarah': 'java',
    'edward': 'c++',
    'paul': 'python',
    }

list_of_people = ['paul', 'sarah', 'elisabeth', 'john', 'edward', 'claudia', 'damian', ]
for name in list_of_people:
    if name in favourite_languages.keys():
        print(f"Hello, {name.title()}! Thank you for your commitment!")
    else:
        print(f"Hello, {name.title()}! You are invited to participate in the survey.")
