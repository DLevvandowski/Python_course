# Ex. 8.9 Messages
# Prepare a list containing a series of short messages, and then pass it to a function called show_messages(), which
# should display each message placed in this list.

def show_messages(messages):
    """Displays messages from the list."""
    for message in messages:
        print(message)


messages_list = ['Hello', 'Stop', 'Attention', 'Exit', 'Wake up', 'Throw away']

show_messages(messages_list)
