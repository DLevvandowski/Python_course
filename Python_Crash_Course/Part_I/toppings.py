# When you want to determine whether two values are unequal, you can use the operator in the form of an exclamation mark
# placed before the equal sign (!=). We will now use another if command to show how to use the operator inequality. We
# will put the expected pizza toppings in a variable, and then let's display a message if the customer did not order a
# pizza with anchovies.

requested_topping = 'mushrooms'

if requested_topping != 'anchovy':
    print("Anchovy, please!")

print('-----')

# The code for this type of action can be created very efficiently by putting the add-ons selected by the customer into
# a list, and then processing this list using a loop. During the execution of the loop, a message will be displayed a
# message indicating the ingredient currently being added to the pizza.

requested_toppings = ['mushrooms', 'bacon', 'double cheese']

for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")

print("\nYour pizza is ready!")
print('-----')

# However, what if the pizzeria runs out of bacon? Placing the if statement inside the for loop allows you to handle
# this kind of situation properly.

requested_toppings = ['mushrooms', 'bacon', 'double cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'bacon':
        print("We're sorry, but we don't have any bacon now.")
    else:
        print(f"Adding {requested_topping}.")

print("\nYour pizza is ready!")
print('-----')

# In the pizzeria program in this case, before we start preparing the pizza, we check whether the list given by the
# customer contains at least one topping. If the list is empty, we display a message asking if he is sure he wants to
# order a pizza without toppings.

requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nYour pizza is ready!")
else:
    print('Are you sure that you want a pizza without toppings?')

print('-----')

# We will now enrich the program by monitoring unusual toppings so that we know about them before we start preparing the
# pizza. The program shown below contains two lists. The first stores the available toppings for the pizza, while the
# second stores the toppings ordered by the customer.

available_toppings = ['mushrooms', 'olives', 'bacon', 'pepperoni', 'pineapple', 'double cheese']

requested_toppings = ['mushrooms', 'fries', 'double cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"We're sorry, but we don't have any {requested_topping} now.")

print("\nYour pizza is ready!")
