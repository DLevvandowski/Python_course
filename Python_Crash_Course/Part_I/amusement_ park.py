# Often it is necessary to check more than just two possible situations. For this purpose, you can use the if-elif-else
# syntax offered by Python. In the listed construction Python executes only one block of code.

# Take, for example, an amusement park where ticket prices are different for different age groups of visitors:
#  The entrance ticket is free for children under 4.
#  The entrance ticket costs $25 for children aged 4 to 18.
#  The entrance ticket costs $40 for those over the age of 18.

age = 12

if age < 4:
    print("The price of admission ticket is $0.")
elif age < 18:
    print("The price of admission ticket is $25.")
else:
    print("The price of admission ticket is $40.")

print("\n-----\n")

# Instead of displaying the price of admission inside the if-elif-else construct, a much better solution would be to set
# in the mentioned construction only the price and place a simple print() call in the program code, the contents of
# which will already be displayed after the if-elif-else construct is executed:

age = 21

if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print(f"The price of admission ticket is ${price}.")

print("\n-----\n")

# Any number of elif blocks can be used in the code. We assume that after reaching 65 years of age, the visitor pays
# only half the normal ticket price.

age = 2

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20

print(f"The price of admission ticket is ${price}.")

print("\n-----\n")

# Python does not require the inclusion of an else block at the end of an if-elif construct. Sometimes the existence of
# an else block is useful, while in other situations it will be much better to use an additional elif command capturing
# a condition of particular interest.

age = 70

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20

print(f"The price of admission ticket is ${price}.")

print("\n-----\n")