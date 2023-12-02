# Ex. 7.2 Restaurant table
# Create a program that asks the customer how many people he wants to book a table for. If the answer is a number
# greater than 8, you should display a message to wait for a table. Otherwise, inform the customer that the table is
# ready.

table = input("Table for how many people? ")
table = int(table)

if table <= 8:
    print("Your table is ready.")
else:
    print("You need to wait a while for a table.")
