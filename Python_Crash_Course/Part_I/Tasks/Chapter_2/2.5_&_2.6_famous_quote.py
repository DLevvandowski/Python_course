# Ex. 2.5
# Find a quote by a famous person you value. Display this quote along with the name of its author.
# The generated output should look like what I have shown below, including the citation marks:
# Albert Einstein once said, "A person who has never made a mistake is someone who has never tried anything new.
#
# Ex. 2.6
# 2.6 Repeat ex. 2.5, but this time put the name of the author of the quote be placed in a variable named famous_person.
# Then prepare message and put it in a new variable named message. Finally, display the message.

first_name = "Bob"
last_name = "Marley"
famous_person = f"{first_name} {last_name}"

message = f'{famous_person} once said: "You never know how strong you are until being strong is your only choice".'
print(message)