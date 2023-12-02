# The int() function converts a number in the form of a text string to a numeric value. How can the int() function be
# used in a real program? Take a look at the following program that determines whether a person is tall enough for a
# train ride.

height = input("How tall are you [cm]? ")
height = int(height)

if height > 90:
    print("\nYou are tall enough for the ride!")
else:
    print("\nYou will be able to take a ride when you grow a bit.")
