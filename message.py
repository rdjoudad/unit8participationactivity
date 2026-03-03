"""
8-9
Messages
Make a list containing a series of short text messages. Pass the list to a function called show_messages(), which prints each 
text message
"""

def show_messages(short_messages):
    for message in short_messages:
        print(message)

short_messages = ["Hello", "How's it going?", "How's work?"]
show_messages(short_messages)