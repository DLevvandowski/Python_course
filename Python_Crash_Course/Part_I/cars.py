# Permanent list sorting

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# Permanent inverted list sorting

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

# Temporary list sorting

cars = ['bmw', 'audi', 'toyota', 'subaru']

print("This is the initial list: ")
print(cars)

print("\nThis is sorted list: ")
print(sorted(cars))

print("\nThis is the initial list again: ")
print(cars, '\n')

# The reverse() method can be used to reverse the original order of the list.

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars, '\n')

cars.reverse()
print(cars, '\n')

# The size of the list can be determined fairly quickly using the len() function.
# Shown below contains four elements, hence its size is 4:

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
print('Length of the list: ', len(cars))

# The following short code snippet shows how the if construction allows you to correctly respond in a certain special
# situation. Car names are valid brand names, so they should practically always be displayed with a capital letter at
# the beginning. However, there are some exceptions and, for example, the value 'bmw' should be all displayed in
# uppercase.

print('-----')
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

print('-----')
