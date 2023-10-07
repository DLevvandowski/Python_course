# Declaring a list of motorcycle brands

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# Changing a list item

motorcycles[0] = 'ducati'
print(motorcycles)

# Adding an element to the end of the list

motorcycles.append('honda')
print(motorcycles)

# Create an empty list and add items to it one by one

motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# A new element can be inserted anywhere in the list, using the insert() method to do so.

motorcycles.insert(0, 'ducati')
print(motorcycles)

# To remove an element from the list can be done based on its position, or its value.
# If you know the location of the item to be removed from the list, you can use the del command.

del motorcycles[0]
print(motorcycles)

# The pop() method removes the last element of the list, but allows you to work with it still after it has been removed.

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()

print(f"The last motorcycle I bought was {last_owned.title()}.")
print(motorcycles)

# The pop() method can also be used to remove any element from the list.
# To do this, specify the index of the element in parentheses.

first_owned = motorcycles.pop(0)
print(f"The first motorcycle I bought was {first_owned.title()}.")
print(motorcycles)

# If the value of the element you want to remove is known, then you can use the method remove().

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

# The remove() method can also be used to work with an element removed from a list.

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'

motorcycles.remove(too_expensive)
print(motorcycles)
print(f"Motorcycle {too_expensive.title()} is too expensive to me.")

