# Ex. 4.1 Pizza
# Think of at least three types of pizza. Put these names in a list, and then display them using a for loop.
#  Modify the for loop so that instead of just the name of the pizza it displays a sentence using that name.
#   For each type of pizza you should have one line of output data containing a simple sentence like:
#   "I like pepperoni pizza".
#  Beyond the loop block, add a sentence at the end of the program stating, how much you like the pizza.
#   The generated output should therefore consist of at least three sentences about your favorite kinds of pizza
#   and one additional sentence like: "I really love pizza!".

pizzas = ['capriciosa', 'pepperoni', 'quattro fromaggi']

for pizza in pizzas:
    print(f'{pizza.title()} is one of the best pizzas in the world!')
print('Pizza is one of my favourite dinner ideas!')