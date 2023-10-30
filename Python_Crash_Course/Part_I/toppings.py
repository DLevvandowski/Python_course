# When you want to determine whether two values are unequal, you can use the operator in the form of an exclamation mark
# placed before the equal sign (!=). We will now use another if command to show how to use the operator inequality. We
# will put the expected pizza toppings in a variable, and then let's display a message if the customer did not order a
# pizza with anchovies.

requested_topping = 'mushrooms'

if requested_topping != 'anchovy':
    print("Anchovy, please!")
