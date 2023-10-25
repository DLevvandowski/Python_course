# Copying the list
# Very often, you want to start work with an existing list and on its basis create a a completely new one.
# To copy the list, you can create a slice containing the entire initial list, which requires skipping the initial
# and final indexes ([:]).

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("\nMy favourite dishes are: ")
print(my_foods)

print("\nMy friend's favourite dishes are: ")
print(friend_foods)

# To prove that we actually have two separate lists, we add a new dish to each list.
# In this way, you can see that each list contains each person's favorite dishes.

my_foods.append('cannolo')
friend_foods.append('icecream')

print("\nMy favourite dishes are: ")
print(my_foods)

print("\nMy friend's favourite dishes are: ")
print(friend_foods)
