# Ex. 8.11 Archived messages
# Start your work with the code created in Exercise 8.10. Call the send_messages() function with a copy of the message
# list. After calling the function, display both lists to show the existence of the original list with the saved
# messages.

def show_messages(msgs):
    """Displays messages from the list."""
    print("\nMessages:")
    for msg in msgs:
        print(msg)


def send_messages(msgs, sent_msgs):
    """Sends messages from the messages_list and transfers them to the sent_messages list."""
    print("\nStarting the messaging process...")
    while msgs:
        current_msg = msgs.pop()
        print(f"Sending message: {current_msg}")
        sent_msgs.append(current_msg)


messages_list = ['Hello', 'Stop', 'Attention', 'Exit', 'Wake up', 'Throw away']
sent_messages = []

show_messages(messages_list)
send_messages(messages_list[:], sent_messages)

print(f"\nMessages list: {messages_list}")
print(f"\nSent messages: {sent_messages}")
