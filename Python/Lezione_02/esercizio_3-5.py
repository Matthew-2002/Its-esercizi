'''3-5. Changing Guest List: You just heard that one of your guests can’t make 
the dinner, so you need to send out a new set of invitations. You’ll have to 
think of someone else to invite.
• Start with your program from Exercise 3-4. Add a print() call at the end of 
your program, stating the name of the guest who can’t make it.

• Modify your list, replacing the name of the guest who can’t make it with the 
name of the new person you are inviting.

• Print a second set of invitation messages, one for each person who is still 
in your list.'''


invitati: list[str] = [
    "Anne Hathaway", 
    "Dante Alighieri", 
    "Einstein", 
    "Gesù"
    ]  
print(f"{invitati[0]} sei stata invitata a cena")
print(f"{invitati[1]} sei stato invitato a cena")
print(f"{invitati[2]} sei stato invitato a cena")
print(f"{invitati[3]} sei stato invitato a cena")

print("-----------")

print(invitati[2],"non sara più invitato")

invitati[2] = "Federer"

print(f"{invitati[0]} sei stata invitata a cena")
print(f"{invitati[1]} sei stato invitato a cena")
print(f"{invitati[2]} sei stato invitato a cena")
print(f"{invitati[3] }sei stato invitato a cena")