# A useful tool for working with numeric values is the modulo (%) operator, which returns the remainder of a number
# division operation.

number = input("Enter number. I'll tell you if this number is even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"Number {number} is even.")
else:
    print(f"Number {number} is odd.")
