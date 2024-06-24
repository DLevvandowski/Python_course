def make_pizza(size, *toppings):
    """Summary information about the prepared pizza"""
    print(f"\nI prepare a {size} cm pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
