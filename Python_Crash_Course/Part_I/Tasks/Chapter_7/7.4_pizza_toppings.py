# Ex. 7.4 Pizza toppings
# Create a loop asking the user to provide a series of pizza toppings. The loop action should terminate when the word
# 'end' is typed. As the user enters more toppings, the loop should display a message that the ingredient has been added
# to the pizza.

message = "\nEnter your pizza topping."
message += "\nIf you end, enter 'end'. "

topping = ""

while topping != 'end':
    topping = input(message)
    if topping != 'end':
        print(f"{topping.title()} was added to pizza.")
    else:
        print("Cya!")
