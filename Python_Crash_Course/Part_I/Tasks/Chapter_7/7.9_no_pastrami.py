# Ex. 7.9 No pastrami
# Use the sandwich_orders list from Exercise 7.8 and make sure that a pastrami sandwich appears in the list at least
# three times. Somewhere at the beginning of the program, place code that displays a message that the bar has run out of
# pastrami, and then use a while loop to remove all occurrences of 'pastrami' from the sandwich_orders list. Make sure
# that no pastrami sandwich is placed in the finished_sandwiches list.

sandwich_orders = ['salmon sandwich', 'pastrami sandwich', 'salami sandwich', 'pastrami sandwich', 'ham sandwich',
                   'cheese sandwich', 'pastrami sandwich']
finished_sandwiches = []

print("\nATTENTION! PASTRAMI IS OUT!\n")

while 'pastrami sandwich' in sandwich_orders:
    sandwich_orders.remove('pastrami sandwich')

while sandwich_orders:
    finished_sandwich = sandwich_orders.pop()
    print(f"{finished_sandwich.title()} is finished.")

    finished_sandwiches.append(finished_sandwich)

print("\n--- Finished sandwiches ---")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())