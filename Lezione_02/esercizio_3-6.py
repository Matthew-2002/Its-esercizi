'''3-6. More Guests: You just found a bigger dinner table, so now more space is available. 
Think of three more guests to invite to dinner.
• Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, 
informing people that you found a bigger table.
• Use insert() to add one new guest to the beginning of your list.
• Use insert() to add one new guest to the middle of your list.
• Use append() to add one new guest to the end of your list.
• Print a new set of invitation messages, one for each person in your list.'''


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