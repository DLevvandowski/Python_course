# The for loop takes a set of elements and then executes a block of code once for each element in the set. The while
# loop, on the other hand, runs as long as the defined condition takes the value True.

current_number = 1

while current_number <= 5:
    print(f"Current number = {current_number}.")
    current_number += 1

# Instead of completely exiting the loop without executing the remaining code in it, you can use the continue command to
# return to the beginning of the loop, based on the result of the conditional test. Take a look at the following loop
# that counts down the numbers from 1 to 10, but only displays on the screen the odd numbers in the specified range.

print('-----')

current_number = 0

while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)
