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
            print (f"{item} sei stata invitata alla mia cena")
        case "Federer":
            print (f"{item} sei stata invitata alla mia cena")
        case "Gesù":
            print (f"{item} sei stata invitata alla mia cena")
        case "Battiato":
            print (f"{item} sei stata invitata alla mia cena")    
        case "Margherita":
            print (f"{item} sei stata invitata alla mia cena")    
        case "Angelo":
            print (f"{item} sei stata invitata alla mia cena")

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