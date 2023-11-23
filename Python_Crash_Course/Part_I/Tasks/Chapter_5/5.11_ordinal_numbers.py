# Ex. 11 Ordinal numbers
# Ordinal numbers indicate the position of an element in a list, for example, first, second, third. In English, most
# such numbers end in "th," except for the numbers 1, 2 and 3.
# » Create a list storing the numbers from 1 to 9.
# » Conduct an iteration through the list.
# » Use the if-elif-else construction inside the loop to correctly display ordinal numbers in English. The generated
# output should be 1st, 2nd, 3rd, 4th, 5th, 6th, 7th, 8th, 9th, and each number should be on a separate line.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

if numbers:
    for number in numbers:
        if number == 1:
            print(f'{number}st')
        elif number == 2:
            print(f'{number}nd')
        elif number == 3:
            print(f'{number}rd')
        else:
            print(f'{number}th')
else:
    print('List of numbers is empty.')
