# Instead of putting a dictionary in a list, sometimes it will be useful to put a list in a dictionary. For example,
# let's consider how to represent a pizza ordered by a customer. If only a list is available, then we can really only
# store the toppings selected by the customer. With a dictionary, on the other hand, the list of toppings will be one of
# the aspects of the pizza about which we can store information.

pizza = {'crust': 'thick', 'toppings': ['mushrooms', 'double cheese']}

print(f" You've ordered {pizza['crust']} crust pizza with the following toppings: ")

for topping in pizza['toppings']:
    print(f"\t{topping}")

# The asterisk in the name of the *toppings parameter tells Python to create an empty tuple named toppings and place the
# resulting values in it.


def make_pizza(size, *toppings):
    """Summary information about the prepared pizza"""
    print(f"\nI prepare a {size} cm pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza(30, 'pepperoni')
make_pizza(40, 'mushrooms', 'green paprica', 'double cheese')
