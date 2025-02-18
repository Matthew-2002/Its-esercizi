n:int = int(input("inserisci la posizione di arrivo: "))
if n % 10 == 1:
    if n == 11:
        print (f"{n}th!")
    else:
        print (f"{n}st!")
elif n % 10 == 2:
    if n == 12:
        print (f"{n}th!")
    else:
        print (f"{n}nd!")
elif n % 10 == 3:
    if n == 13:
        print (f"{n}th!")
    else:
        print (f"{n}rd!")
else:
    print (f"{n}th!")