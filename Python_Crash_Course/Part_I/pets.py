# We assume that there is a list of animals in which the element 'cat' repeatedly appears. To remove all occurrences of
# this value, we can use a while loop as long as the value 'cat' is in the list, as I have shown in the following
# program.

pets = ['dog', 'cat', 'dog', 'gold fish', 'cat', 'rabbit', 'hamster', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

# When calling a function, Python must match each argument in the call with a parameter found in the function
# definition. The simplest solution to this problem uses the order of the supplied arguments. Values matched in this way
# are called positional arguments.
# To see how this works, consider a function that displays information about an animal. The function discussed here
# gives the type of animal and its name, as I have shown in the following code snippet.

print("-----")
def describe_pet(animal_type, pet_name):
    """Displays information about animal."""
    print(f"\nMy pet is {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet("dog", "lucifer")
describe_pet("cat", "garfield")

# You can define the name and its value directly in the argument, so there should be no confusion when passing this kind
# of argument to the function (that is, you will not get a message regarding a lucifer animal named Dog).

print("-----")
describe_pet(pet_name="lucifer", animal_type="dog")

# Note: When using keyword arguments, make sure you use exactly the same parameter names as in the function definition.

# In the following code snippet, we will modify the definition of the describe_pet() function to include the default
# value 'dog' for the animal_type parameter. Therefore, calling the function without an argument for animal_type will
# cause Python to use the value 'dog' for this parameter.
print('-----')
def describe_pet(pet_name, animal_type="dog"):
    """Displays information about animal."""
    print(f"\nMy pet is {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name="lucifer")

# Since positional arguments, keyword arguments and default values can be used together, there are very often multiple
# ways to call the same function.

print('-----')

# Dog named Lucifer
describe_pet('lucifer')
describe_pet(pet_name='lucifer')

# Cat named Garfield
describe_pet('garfield', 'cat')
describe_pet(pet_name='garfield', animal_type='cat')
describe_pet(animal_type='cat', pet_name='garfield')

# Note - It is completely irrelevant which function call style you choose. If the function generates output as expected,
# use whichever call style you find easiest to understand.
