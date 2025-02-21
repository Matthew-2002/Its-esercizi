'''3-6. More Guests: You just found a bigger dinner table, so now more space is available. 
Think of three more guests to invite to dinner.
• Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, 
informing people that you found a bigger table.
• Use insert() to add one new guest to the beginning of your list.
• Use insert() to add one new guest to the middle of your list.
• Use append() to add one new guest to the end of your list.
• Print a new set of invitation messages, one for each person in your list.'''


invitati:list[str] = ["Anne Hathaway", "Dante Alighieri", "Einstein", "Gesù"]
print (f"{invitati[0]} sei stata invitata a cena")
print (f"{invitati[1]} sei stato invitato a cena")
print (f"{invitati[2]} sei stato invitato a cena")
print (f"{invitati[3]} sei stato invitato a cena")

print ("-----------")

print(invitati[2],"non sara più invitato")

invitati[2] = "Federer"

print (f"{invitati[0]} sei stata invitata a cena")
print (f"{invitati[1]} sei stato invitato a cena")
print (f"{invitati[2]} sei stato invitato a cena")
print (f"{invitati[3]} sei stato invitato a cena")

print ("-----------")

print("è stato trovato un tavolo più grande, inviterò altre tre persone")

invitati.insert (0, "Battiato")
metà:int = len(invitati) //2
invitati.insert (metà, "Margherita")
invitati.append ("Angelo")

print (f"{invitati[0]} sei stato invitato a cena")
print (f"{invitati[1]} sei stata invitata a cena")
print (f"{invitati[2]} sei stata invitata a cena")
print (f"{invitati[3]} sei stato invitato a cena")
print (f"{invitati[4]} sei stato invitato a cena")
print (f"{invitati[5]} sei stato invitato a cena")
print (f"{invitati[6]} sei stato invitato a cena")