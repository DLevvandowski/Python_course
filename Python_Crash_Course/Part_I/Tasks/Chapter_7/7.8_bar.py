# Ex. 7.8 Bar
# Prepare a list named sandwich_orders and put the names of different sandwiches on it. Then prepare an empty list named
# finished_sandwiches. Iterate through the list of ordered sandwiches and display information about a particular order,
# for example: "A tuna sandwich has been prepared." When the sandwich is done, the item representing it should be moved
# to the finished_sandwiches list. Once the sandwich_orders list is empty, display a message listing all made
# sandwiches.

sandwich_orders = ['salmon sandwich', 'salami sandwich', 'ham sandwich', 'cheese sandwich']
finished_sandwiches = []

while sandwich_orders:
    finished_sandwich = sandwich_orders.pop()
    print(f"{finished_sandwich.title()} is finished.")

    finished_sandwiches.append(finished_sandwich)

print("\n--- Finished sandwiches ---")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())
