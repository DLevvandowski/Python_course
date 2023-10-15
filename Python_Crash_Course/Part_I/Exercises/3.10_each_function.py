# Ex. 3.10 Each function
# Think about what information you could include in a list. For example, create a list of mountains, rivers,
# countries, cities, languages or anything other. Prepare a program that will create a list storing this information
# and use at least once each function introduced in this chapter.

italian_cities = ['roma', 'firenze', 'milano', 'napoli', 'sicilia', 'venezia', 'verona', 'bolognese', 'palermo']
print('This is initial list of Italian cities that I would like to visit: ', italian_cities, '\n')

print('Number of Italian cities in my list is: ', len(italian_cities), '\n')

print('This is my list temporary alphabetically sorted: ', sorted(italian_cities), '\n')

print('This is my list temporary alphabetically sorted and reversed: ', sorted(italian_cities, reverse=True), '\n')

italian_cities.reverse()
print('This is my list reversed: ', italian_cities, '\n')

italian_cities.sort(reverse=True)
print('This is my list reversed alphabetically and permanently sorted: ', italian_cities, '\n')

italian_cities.sort()
print('This is my list alphabetically and permanently sorted: ', italian_cities, '\n')

print(f'{italian_cities[8].title()} is city I would like to visit the least, so I delete it from my list.\n')
del italian_cities[8]

print('This is my new list: ', italian_cities, '\n')

print(f'{italian_cities[5].title()} is the capital of Italy.\n')
