'''3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, 
and now you have space for only two guests.
• Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only 
two people for dinner.
• Use pop() to remove guests from your list one at a time until only two names remain in your list. 
Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t 
invite them to dinner.
• Print a message to each of the two people still on your list, letting them know they’re still invited.
• Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure y
ou actually have an empty list at the end of your program.'''


invitati:list = ["Anne Hathaway", "Dante Alighieri", "Einstein", "Gesù"]  
for item in invitati:
    print (f"{item} sei stato/a invitato/a alla mia cena")

print ("Einstein")
invitati [invitati.index("Einstein")] = "Federer"
for item in invitati:
    print (f"{item} sei stato/a invitato/a alla mia cena")

print("è stato trovato un tavolo più grande, inviterò altre tre persone")
invitati.insert (0, "Battiato")
invitati.insert (2, "Margherita")
invitati.append ("Angelo")
for item in invitati:
    match item:
        case "Anne Hathaway":
            print (f"{item} sei stata invitata alla mia cena")
        case "Dante Alighieri":
            print (f"{item} sei stato invitato alla mia cena")
        case "Federer":
            print (f"{item} sei stato invitato alla mia cena")
        case "Gesù":
            print (f"{item} sei stato invitato alla mia cena")
        case "Battiato":
            print (f"{item} sei stato invitato alla mia cena")    
        case "Margherita":
            print (f"{item} sei stata invitata alla mia cena")    
        case "Angelo":
            print (f"{item} sei stato invitato alla mia cena")

print ("ho scoperto che potrò invitare solo due persone alla cena")
while len(invitati) > 2:
    item = invitati [-1]
    invitati.pop()
    print (f"Perdonami {item} purtroppo non potrai venire alla cena")
for item in invitati:
    print (f"{item} sei ancora invitato/a alla mia cena")
del invitati [1]
del invitati [0]
print (invitati)