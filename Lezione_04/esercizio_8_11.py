'''8-11. Archived Messages: Start with your work from Exercise 8-10. 
Call the function send_messages() with a copy of the list of messages. 
After calling the function, print both of your lists to show that the 
original list has retained its messages.'''



# defyning functions

def show_messages(messages:list[str]):
    for item in messages:
        print(item)


def send_messages(messages):
    sent_messages:list[str] = []
    for i in range(len(messages)):
        print(messages[-1])
        sent_messages.append(messages[-1])
        messages.pop()
    
        
    return sent_messages


# code 


messages: list[str] = ["Ciao", "Come stai?", "Spero tutto bene"]
print("Messages:\n")
show_messages(messages)

print("-----")

print("Sent Messages:\n", *send_messages(messages))
print("Messages after send_messages:\n",*messages)

print("-----")

'''print("Messages after send_messages: \n",*messages)

print("-----")

print("Sent Messages:\n",*sent_messages)

#print(*send_messages(messages=["Ciao", "Come stai?", "Spero tutto bene"]))'''






