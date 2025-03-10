'''8-10. Sending Messages: Start with a copy of your program 
from Exercise 8-9. Write a function called send_messages() 
that prints each text message and moves each message to a 
new list called sent_messages as it’s printed. After calling 
the function, print both of your lists to make sure the 
messages were moved correctly.'''


messages: list[str] = ["Ciao", "Come stai?", "Spero tutto bene"]

def show_messages():
    for item in messages:
        print(item)

show_messages()

print("------")

def send_messages():
    sent_messages= messages[:]
    for item in sent_messages:
        print(item)
        messages.remove(item) 
    print(messages)
    print(sent_messages)

send_messages()
