# Ex. 3.4 Guest list
# If you could invite anyone to dinner, living or deceased, who would you invite?
# Create a list with at least three people you would want to invite to dinner.
# Then use this list to display a message for each of these people inviting them to dinner.

guests = ['Klaudia Lewandowska', 'Gal Gadot', 'Scarlett Johansson']

print(f"Invitation to dinner for {guests[0]}.")
print(f"Invitation to dinner for {guests[1]}.")
print(f"Invitation to dinner for {guests[2]}.")

# Ex. 3.5 Change guest list
# You have learned that one of the invited people cannot come to dinner.
# It is therefore necessary to send further invitations.
# Think about who else you will invite in this case.
#  Start your work with the program created in exercise 3.4. At its end, place a print() command displaying
#   a message with information, which of the invited guests cannot come.
#  Modify the list and data of the guest who will not be able to come to the dinner,
#   replace with the data of the new invited person.
#  Display a second set of invitation messages, one message for each person on the list.

print(f"\nSorry, but {guests[2]} cannot come to dinner.")

guests[2] = 'Caterina Scorsone'

print(f"\nInvitation to dinner for {guests[0]}.")
print(f"Invitation to dinner for {guests[1]}.")
print(f"Invitation to dinner for {guests[2]}.")

# Ex. 3.6 More guest
# You've found a bigger table, which means more room for guests. So think about three more people you could invite
# for dinner.
#  Start your work with the program created in exercises 3.4 and 3.5.
#   At the end of it, place a print() command displaying a message about finding a larger table.
#  Using the insert() method, add a new guest to the beginning of the list.
#  Using the insert() method, add a new guest in the middle of the list.
#  Use the append() method to add a new guest at the end of the list.
#  Display a new set of invitation messages, one message for each person on the list.

print("\nA larger table has been found.")

guests.insert(0, 'Stefania Spampinato')
guests.insert(2,'Kim Raver')
guests.append('Tricia Helfer')

print(f"\nInvitation to dinner for {guests[0]}.")
print(f"Invitation to dinner for {guests[1]}.")
print(f"Invitation to dinner for {guests[2]}.")
print(f"Invitation to dinner for {guests[3]}.")
print(f"Invitation to dinner for {guests[4]}.")
print(f"Invitation to dinner for {guests[5]}.")

# Ex. 3.7 Shrinking guest list
# It turned out that the larger table will not be delivered on time, and therefore you have room for only two guests.
#  Start your work with the program created in Exercise 3.6.
#   Add a new line displaying the message that you can invite only two people to dinner.
#  Using the pop() method, remove one guest at a time from the list until only two people remain on the list.
#   After removing each person, display a message intended for him/her with an apology
#   for not being able to invite her to dinner.
#  Display a personalized message with a dinner invitation to the two people remaining on the list.
#  Use the del command to remove the last two people from the list, which should thus become empty.
#   Finally, display the list to make sure it is indeed empty.

print("\nSorry, but you can invite only two people...")

popped_person = guests.pop()
print(f"\n{popped_person} I regret to have to cancel the invitation. I apologize for this.")

popped_person = guests.pop()
print(f"\n{popped_person} I regret to have to cancel the invitation. I apologize for this.")

popped_person = guests.pop()
print(f"\n{popped_person} I regret to have to cancel the invitation. I apologize for this.")

popped_person = guests.pop()
print(f"\n{popped_person} I regret to have to cancel the invitation. I apologize for this.")

print(f"\nInvitation to dinner for {guests[0]}.")
print(f"Invitation to dinner for {guests[1]}.")

del guests[0]
del guests[0]

print(guests)
