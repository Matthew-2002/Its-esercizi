'''3-2. Greetings: Start with the list you used in Exercise 3-1, 
but instead of just printing each person’s name, print a message to them. 
The text of each message should be the same, but each message should be 
personalized with the person’s name.'''


names:list[str] = ["Lorenzo", "Angelo", "Ares", "Ottavio"] 
for item in names:
    print (f"{item} sei stato invitato alla mia festa")