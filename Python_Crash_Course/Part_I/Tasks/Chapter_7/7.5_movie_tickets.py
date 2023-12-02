# Ex. 7.5 Movie tickets
# The price of a movie ticket depends on the age of the viewer. If the viewer is under 3 years old, the ticket is free.
# For children between the ages of 3 and 12, the ticket costs $10. For those over 12 years of age, the ticket price is
# $15. Create a loop asking the user to enter the age, and then display a message with the correct ticket price based on
# the received data.

message = "\nHow old are you?"
message += "\nEnter 'end' to exit. "

price = ""

while price != "end":
    price = input(message)
    if price == "end":
        print("Enjoy the seance!")
        break

    price = int(price)

    if price < 3:
        print("Ticket for you is free!")
    elif price <= 12:
        print("Ticket for you cost $10.")
    else:
        print("Ticket for you cost $15.")
