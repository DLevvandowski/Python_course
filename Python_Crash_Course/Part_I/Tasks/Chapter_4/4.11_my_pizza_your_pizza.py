# Ex. 4.11 My pizza, your pizza
# Start your work with the program created in Exercise 4.1 earlier in the chapter. Create a copy of the list with
# pizzas and name it friend_pizzas. Now perform the tasks listed below:
#  Add a new pizza to the initial list.
#  Add a pizza (different from the one in the previous section) to the friend_pizzas list.
#  Verify that you actually have two separate lists. Display the message "My favorite types of pizzas are:" and
# then use a for loop to display the contents of the first list. Now display the message "My friend's favorite
# types of pizza are:" and use the for loop to display the contents of the second list. Make sure that each new pizza
# is placed in the corresponding list.

pizzas = ['capriciosa', 'pepperoni', 'quattro fromaggi']
friend_pizzas = pizzas[:]

pizzas.append('diavola')
friend_pizzas.append('spinachi')

print('\nMy favourite pizzas are: ')
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favourite pizzas are: ")
for pizza in friend_pizzas:
    print(pizza)
