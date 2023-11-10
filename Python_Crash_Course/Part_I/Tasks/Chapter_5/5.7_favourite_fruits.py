# Ex. 5.7 Favourite fruits
# Prepare a list of your favorite fruits. Then create a series of independent if statements to check the presence of
# specific fruits in the list.
#  Create a list named favorite_fruits and put three favorite fruits.
#  Create five if statements. Each should check for the presence of a certain type of fruit. If the fruit is in the
#   list, in the if block should display a message like: "You really like bananas!".

favourite_fruits = ['banana', 'mango', 'passion fruit']

type_of_fruit = 'banana'
if type_of_fruit in favourite_fruits:
    print(f"You really like {type_of_fruit}s!")

type_of_fruit = 'apple'
if type_of_fruit in favourite_fruits:
    print(f"You really like {type_of_fruit}s!")

type_of_fruit = 'orange'
if type_of_fruit in favourite_fruits:
    print(f"You really like {type_of_fruit}s!")

type_of_fruit = 'mango'
if type_of_fruit in favourite_fruits:
    print(f"You really like {type_of_fruit}s!")

type_of_fruit = 'passion fruit'
if type_of_fruit in favourite_fruits:
    print(f"You really like {type_of_fruit}s!")
