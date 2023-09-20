# importing modules

import random
import sys

# This is my first program in Python
# print() - print data on the screen

print("This is my first program in Python")

# To comment something in multiple lines use '''[comment]'''
'''
Multiline comment
'''

# Variable is a place to store values
# The name of a variable is like a label for that value

name = "Python student"

print(name)

# Name of variable can contain letters or numbers
# It cannot start with a number!

# There is 5 data types: Numbers, Strings, List, Tuples, Dictionary
# You can store any of them in the same variable

number = 15
print(number)

# There is few arithmetical operators -> +, -, *, /, %, **, //
# Addition -> +
# Subtraction -> -
# Multiplication -> *
# Division -> /
# Rest of division, modulo -> %

# Examples of exponential calculations
print("2 + 2 = ", 2 + 2)
print("2 - 2 = ", 2 - 2)
print("2 * 2 = ", 2 * 2)
print("2 / 2 = ", 2 / 2)
print("20 ** 2 = ", 20 ** 2)
print("100 // 2 = ", 100 // 2)

# The order of operations * and / is performed before + and -.
print("5 + 5 - 5 * 5 = ", 5 + 5 - 5 * 5)
print("(5 + 5 - 5) * 5 = ", (5 + 5 - 5) * 5)

# If you need to use a "quotation mark", use the "\" (backslash) character to display it

motto = "Motto of the day: \"The only way to learn a new programming language is to write programs in it.\""
print(motto)

# Multiline motto

multilineMotto = '''Motto of the day: \"The only way to learn a new programming language 
is to write programs in it..\"'''

print(multilineMotto)

# To embed a string in the console output use %s

print("%s %s %s" % ('I really like this motto! ', motto, multilineMotto))

# To avoid printing new lines use end = " "
print("I like", end="   ")
print("Python")

# You can display a string multiple times with *

print("\n" * 5)

# LISTS
# List allows you to create a list of values and manipulate them
# Each value has an index, with the first starting at 0!

shoppingList = ['Eggs', 'Cheese', 'Tomatoes', 'Chilli']

print('The most important ingredient in scrambled eggs is -> ', shoppingList[0])
print('Optional ingredient for scrambled eggs is -> ', shoppingList[3])

# You can change the value stored in the list field
shoppingList[0] = "Frozen vegetables"
print(shoppingList)

# You can change the value so that you get a subset of the list

print(shoppingList[1:3])

# You can put any data type in a list, including a list

otherActivities = ['Cleaning house', 'Watching TV', 'Learning to program']
toDo = [otherActivities, shoppingList]

print(toDo)

# Get the second item on the second list

print(toDo[1][1])

# [name_of_list].append - Add the item to the list

shoppingList.append('lemon')
print(toDo)

# [name_of_list].insert - Add an item to the list at the given index
shoppingList.insert(3, 'ketchup')
print(shoppingList)

# [name_of_list].remove - Remove an item from a list with a given value

shoppingList.remove("ketchup")

print(shoppingList)

# [name_of_list].sort - Sort list items

shoppingList.sort()

print(shoppingList)

# [name_of_list].reverse - Reverse the sorting of the items in the list

shoppingList.reverse()

print(shoppingList)

# del [name_of_list][number_of_index] - Remove an item from a list with a given index

del shoppingList[4]
print(shoppingList)

# We can combine lists using +
toDo = otherActivities + shoppingList
print(toDo)

# len - Obtain list length
print(len(toDo))

# Obtain the maximum item from the list
print(max(toDo))

# Obtain the minimum item from the list
print(min(toDo))

# TUPLES
# Values in a tuple cannot change like lists
# In contrast, list items are numbered from zero
# Lists are a modifiable type and therefore their elements can be changed at will.
# A tuple is generally a list that cannot be modified.

piTuple = (3, 1, 4, 1, 5, 9)

# Convert a tuple to a list
newTuple = list(piTuple)

# Tuples also have:
# -> a length (len[tuple])
# -> a minimum element (min[tuple])
# -> a maximum element (max[tuple])

print(len(piTuple))

# DICTIONARY / MAP
# The dictionary consists of values with a unique key for each value.
# It is similar to a list.

superHeroes = {'Batman': 'Superman',
               'Ironman': 'Robin',
               'Wizard': 'Deadpool'}

print(superHeroes)

# To delete entry use del [name_of_dictionary[value]]

del superHeroes['Wizard']
print(superHeroes)

# To replace the value of dictionary use [name_of_dictionary[value]] = [new_value]
superHeroes['Wizard'] = 'Spider man'
print(superHeroes)

# Display the number of elements in the dictionary
print(len(superHeroes))

# Get a list of dictionary keys
print(superHeroes.keys())

# Get a list of dictionary values
print(superHeroes.values())

# Conditional instructions
# if, else and elif are used for various activities - actions based on conditions
# Comparison operators: ==, !=, >, <, >=, <=

# if instruction will execute the code if the condition is met
# Whitespace characters are used to group blocks of code in Python
# Use the same number of consecutive spaces for blocks of code

age = 28
if age > 18:
    print('You can do the license!')

# Use if-else instruction if you want to independently execute other code
if age > 18:
    print('You can do the license!')
else:
    print('You are too young to become a driver!')

# If you want to check multiple conditions, use elif
# If the first element is true, it will not check the other conditions

if (age >= 1) and (age <= 35):
    print('It is your birthday!')
elif (age == 35) or (age >= 65):
    print('It is your birthday now!')
elif not (age == 30):
    print("It is not your birthday!")

# FOR loop
# Allows you to perform an action a certain number of times

for x in range(0, 20):
    print(x, ' ', end="")

print('\n')

# You can use a FOR loop to go through the list

shoppingList = ['Eggs', 'Cheese', 'Tomatoes', 'Chilli']

for y in shoppingList:
    print(y)

# You can also define a list of numbers to go through all the elements
listOfNumbers = [[2, 5, 10], [20, 50, 100], [200, 500, 1000]]

for x in range(0, 3):
    for y in range(0, 3):
        print(listOfNumbers[x][y])

# WHILE loop
# Useful when you don't know ahead of time how many times the loop will need to be executed

randomNumber = random.randrange(0, 1000)

while randomNumber != 500:
    print(randomNumber)
    randomNumber = random.randrange(0, 1000)

# The while loop interator is defined before the loop!

i = 0
while i <= 10:
    if i % 2 == 0:
        print(i)
    elif i == 9:
        # break - Forces termination of all loops
        break
    else:
        # Shortcut for i=i+1 ->
        i += 1
        # continue - Goes to the next iteration of the loop
        continue

    i += 1

# FUNCTIONS
# Allow you to reuse and write readable code.
# Type def (define) the name of the function and the parameters received.
# Return is used to return a parameter or value

def addFunction(num1, num2):
    addResult = num1 + num2
    return addResult

print(addFunction(5, 10))

# If you define a variable outside a function, it will work anywhere

totals = 0

def subFunction(num1, num2):
    subResult = num1 - num2
    return subResult

print(subFunction(21, 6))

# I/O Input
print('Will you tell me your name?')
# Stores everything you have typed until called by the ENTER key

name = sys.stdin.readline()

print('Hello, ', name)

# Strings
longString = "Worry about what other people think of you, and you will always be their prisoner. - Lao Tzu"

# Take the first 4 characters of the sentence

print(longString[0:4])

# Print the last 5 characters
print(longString[-5:])

# All up to the last 5 characters
print(longString[:-5])

# Connects the parts of the string
print(longString[:4] + " <-> epic quote")

# Formatting strings
print("%c is my letter %s, my %d number is %.5f" % ('X', 'favourite', 1, .16))

# The first letter begins with a capital letter
print(longString.capitalize())

# Returns the index of the beginning of the string
# Is case-sensitive

print(longString.find('people'))

# Returns true if all characters are letters | -> is not a letter
print(longString.isalpha())

# Returns the length of the string
print(len(longString))

# Replace the first word with the second (Add a number to replace more)
print(longString.replace('people', 'rivals'))

# Removing spaces from the front and end
print(longString.strip())

# Split the string into a list based on the given separator
quoteList = longString.split(' ')
print(quoteList)

# Files I/O
# Write or create a file to save
testFile = open("test.text", "wb")

# Download the file type used
print(testFile.mode)

# Write text to file with new line
testFile.write(bytes("How to occupy a programmer?\n - Read the sentence below.\n - "
                     "Read the sentence above.\n", 'UTF-8'))

# Closes file
testFile.close()

# Opens file for reading and writing
testFile = open('test.text', 'r+')

# Read/display text from file
testFile = testFile.read()

print(testFile)

print(testFile.find('sentence'))

# CLASSES AND OBJECTS
# The concept of object-oriented programming (OOP) allows us to model things from the real world using code
# Each object has certain attributes (e.g., color, height, weight), which are object variables

'''
Classes allow us to combine data and functions. Creating a new class creates a new type of object,
allowing new instances of that type to be created. 
Attributes can be attached to each instance of a class to maintain its state.
Instances of a class can also have methods (defined by its class) o modify the state.
'''

# An object is simply a collection of data (variables) and methods (functions) that operate on that data.
# Similarly, a class is a blueprint for that object.


class Human:

    # 'None' means no value
    # You can set a variable as private by starting with __

    __name = None
    __height = None
    __weight = None
    __language = None

    # Constructor is called to set or initialize an object
    # self -> allows an object to refer to itself inside a class

    def __init__(self, names, height, weight, language):
        self.__name = names
        self.__height = height
        self.__weight = weight
        self.__language = language

    def set_name(self, names):
        self.__name = names

    def set_height(self, height):
        self.__height = height

    def set_weight(self, weight):
        self.__weight = weight

    def set_language(self, language):
        self.__language = language

    def take_name(self):
        return self.__name

    def take_height(self):
        return self.__height

    def take_weight(self):
        return self.__weight

    def take_language(self):
        return self.__language

    def takeType(self):
        print('Human')

    def toString(self):
        return "{} has {} cm height, {} kg weight and program in {}".format(self.__name, self.__height,
                                                                            self.__weight, self.__language)


# How to create a human being? (object)

programmer = Human('Damian', 180, 98, 'Python, Java')

print(programmer.toString())

# Inheritance
# You can inherit all variables and methods from another class - example below

class Driver(Human):
    __company = None

    def __init__(self, names, height, weight, language, company):
        self.__company = company
        self.__takeType = None

        # How to call a superclass constructor?
        super(Driver, self).__init__(names, height, weight, language)

    def setCompany(self, company):
        self.__company = company

    def takeCompany(self):
        return self.__company

    # This way you can override functions in the superclass:
    def takeType(self):
        print("Driver")

    def toString(self):
        return "{} has {} cm height, {} kg weight and programs in {}. He works in {}".format(self.take_name(),
                                                                                             self.take_height(),
                                                                                             self.take_weight(),
                                                                                             self.take_language(),
                                                                                             self.__company)

mike = Driver("Mike", 190, 96, "Python (a little)", "DPD")

print(mike.toString())

# Polymorphism
# Allows objects to be specified as their superclasses

class HumanTest:
    @staticmethod
    def takeType(human):
        human.takeType()

tested_Human = HumanTest()
tested_Human.takeType(programmer)
tested_Human.takeType(mike)