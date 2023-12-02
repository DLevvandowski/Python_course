# Ex. 7.6 Three outputs
# Prepare three different versions of Exercise 7.4 or Exercise 7.5, each of which will perform the following tasks at
# least once:
# » Using the conditional test in a while loop to stop its operation.
# » Using the active variable to control the length of the while loop.
# » Using the break command to exit the loop when the user types 'end'.

print("\nFirst  task: ")
message = "\nEnter your pizza topping."
message += "\nIf you end, enter 'end'. "

topping = ""

while topping != 'end':
    topping = input(message)
    if topping != 'end':
        print(f"{topping.title()} was added to pizza.")
    else:
        print("Cya!")

print("\nSecond task: ")
message = "\nEnter your pizza topping."
message += "\nIf you end, enter 'end'. "

active = True

while active:
    topping = input(message)
    if topping != 'end':
        print(f"{topping.title()} was added to pizza.")
    else:
        print("Cya!")
        active = False

print("\nThird task: ")
message = "\nEnter your pizza topping."
message += "\nIf you end, enter 'end'. "

topping = ""

while topping != "end":
    topping = input(message)
    if topping != 'end':
        print(f"{topping.title()} was added to pizza.")
    else:
        print("Cya!")
        break
