"""
8-9
Messages
Make a list containing a series of short text messages. Pass the list to a function called show_messages(), which prints each 
text message.
"""

def show_messages(short_messages):
    if not short_messages:
        print("no messages to print")
        return
    for message in short_messages:
        print(message)


def send_messages(unsent_messages, sent_messages):
    while unsent_messages:
        message = unsent_messages.pop()
        print(f"Sending:\n{message}")
        print()
        sent_messages.append(message)

short_messages = ["Hello", "How's it going?", "Lovely weather we're having"]
sent_messages = []
send_messages(short_messages, sent_messages)

show_messages(short_messages)
show_messages(sent_messages)


"""
8-10. 
Sending Messages
Start with a copy of your program from Exercise 8-9. Write a function called send_messages() that prints each text message and moves each message to a new list
called sent_messages as it's printed. After calling the function, print both of your lists to make sure the messages
were moved correctly.
"""

"""
8-11. 
Archived Messages
Start with your work from Exercise 8-10. Call the function send_messages() with a copy of the list of messages. 
After calling the function, print both of your lists to show that the original list has retained its messages.
"""
short_messages = ["Hello", "How's it going?", "Lovely weather we're having"]
sent_messages = []

send_messages(short_messages[:], sent_messages)

print("Original list: ")
show_messages(short_messages)

print("\nOther list: ")
show_messages(sent_messages)

