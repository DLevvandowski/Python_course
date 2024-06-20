# Ex. 8.12 Sandwiches
# Create a function that accepts a list of ingredients that the customer wants in the sandwich they are ordering. The
# function should contain one parameter storing anu number of arguments passed in the function call, and display a
# summary about the sandwich ordered. Call the prepared function three times, each time with a different number of
# arguments.

def make_sandwich(*ingredients):
    print("\nYou ordered a sandwich with the following ingredients: ")
    for ingredient in ingredients:
        print(f" - {ingredient}")
    print('Enjoy!')


make_sandwich('butter', 'tomatoes', 'salt', 'pepper')
make_sandwich('ham', 'cheese', 'ketchup')
make_sandwich('pesto', 'tomatoes', 'mozzarella', 'italian herbs')
