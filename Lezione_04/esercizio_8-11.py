'''8-11. Archived Messages: Start with your work from Exercise 8-10. 
Call the function send_messages() with a copy of the list of messages. 
After calling the function, print both of your lists to show that the 
original list has retained its messages.'''



messages: list[str] = ["Ciao", "Come stai?", "Spero tutto bene"]

def show_messages():
    for item in messages:
        print(item)

show_messages()

print("------")

def send_messages(messages, sent_messages=messages[:]):
    for item in sent_messages:
        print(item)
        messages.remove(item) 
            
    return(messages, sent_messages)


print(*send_messages(messages))

print("-----")

print(*send_messages(messages=["Ciao", "Come stai?", "Spero tutto bene"]))






