# Ex. 5.2 More conditional tests
# You don't have to limit yourself to just 10 tests. If you want to try other comparisons, create more tests and put
# them in the file more_conditional_tests.py. You should get at least one True and False result for the tests listed
# below:
#  Test for equality and inequality of text strings.
#  Test using the lower() function.
#  Numerical tests involving equality and inequality checking, operations greater than and less than, as well as
#   greater than or equal to and less than or equal.
#  Tests using the keywords and and or.
#  Checking whether an element is in a list.
#  Checking if an element is not in a list.

print('\nTEST 1')
bigger_dog = 'labrador'
print("Are yorkies bigger than labradors?")
print(bigger_dog == 'yorkie')
print("Are labradors bigger than yorkies?")
print(bigger_dog != 'yorkie')

print('\nTEST 2')
user = 'Cocoobongoo'
print("Is there a registered Cocoobongoo account?")
print(user == 'cocoobongoo')
print("Is there a registered Cocoobongoo account? (using lower() function)")
print(user.lower() == 'cocoobongoo')

print('\nTEST 3')
age = 28
print("Is the person's age 28?")
print(age == 28)
print("Is the person not 28 years old?")
print(age != 28)
print("Is the person more than 25 years old?")
print(age > 25)
print("Is the person less than 20 years old?")
print(age < 20)
print("Is the person's age greater than or equal to 28?")
print(age >= 28)
print("Is the person's age less than or equal to 27?")
print(age <= 27)

print('\nTESTS 4 & 5')
pepperoni_pizza = ['mozzarella', 'pepperoni', 'tomato sauce']
print('Pepperoni pizza ingredients: ', pepperoni_pizza)
ingredient_1 = 'pineapple'
ingredient_2 = 'pepperoni'
ingredient_3 = 'mozzarella'
ingredient_4 = 'ham'

print("Is pineapple not on the ingredient list for pepperoni pizza?")
if ingredient_1 not in pepperoni_pizza:
    print(True)
else:
    print(False)
print("Is pepperoni not on the ingredient list for pepperoni pizza?")
if ingredient_2 not in pepperoni_pizza:
    print(True)
else:
    print(False)

print("Is mozzarella on the ingredient list for pepperoni pizza?")
if ingredient_3 in pepperoni_pizza:
    print(True)
else:
    print(False)
print("Is ham on the ingredient list for pepperoni pizza?")
if ingredient_4 in pepperoni_pizza:
    print(True)
else:
    print(False)