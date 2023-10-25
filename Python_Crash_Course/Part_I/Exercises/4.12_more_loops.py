# Ex. 4.12 More loops
# In all the foods.py programs presented in this chapter, I have avoided using for loops to save some space.
# Choose any version of the foods.py program, then create two for loops to display both lists of foods.

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannolo')
friend_foods.append('icecream')

print("\nMy favourite dishes are: ")
for food in my_foods:
    print(food)

print("\nMy friend's favourite dishes are: ")
for food in friend_foods:
    print(food)
