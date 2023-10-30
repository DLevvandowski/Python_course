# Ex. 3.8 Explore the world
# Think of five places in the world that you would like to visit.
#  Put all the places on the list and make sure it is not arranged alphabetically.
#  Display the list in its original order. Don't worry about elegantly displaying the list,
#   just display it as a regular Python list.
#  Use the sorted() function to display the list in alphabetical order without modifying the actual list.
#  Display the initial list again to show that it has not been modified.
#  Use the sorted() function to display the list in reverse alphabetical without modifying the actual list.
#  Redisplay the initial list to show that it has not been modified.
#  Use the reverse() method to change the order of the list, and then display it to confirm the reorder.
#  Use the reverse() method again to reorder the list. Display it to show that it has reverted to the original order.
#  Use the sort() method to change the order of the list to alphabetical, and then display it to confirm the reorder.
#  Use the sort() method to change the order of the list to reverse alphabetical,
#   and then display it to confirm the reorder.

places = ['new york', 'rome', 'london', 'paris', 'firenze']
print(places, '\n')

print(sorted(places), '\n')

print(places, '\n')

print(sorted(places, reverse=True), '\n')

print(places, '\n')

places.reverse()
print(places, '\n')

places.reverse()
print(places, '\n')

places.sort()
print(places, '\n')

places.sort(reverse=True)
print(places, '\n')