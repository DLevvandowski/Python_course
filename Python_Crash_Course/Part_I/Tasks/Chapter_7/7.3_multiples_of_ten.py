# Ex. 7.3 Multiples of ten
# Ask the user to enter any number and then check if it is a multiple of 10.

number = input("Enter a number: ")
number = int(number)

if number % 10 == 0:
    print(f"\nNumber {number} is a multiple of 10.")
else:
    print(f"\nNumber {number} isn't a multiple of 10.")
