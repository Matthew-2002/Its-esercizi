'''Esercizio 3C-10. Scrivere un programma in Python che permetta 
all'utente di inserire una data (giorno e mese espressi in forma 
numerica), salvi la data in una tupla e utilizzi un match statement 
per verificare se la data corrisponde a una festività o a un evento 
speciale:
'''


mesi30: list[int] = [11, 4, 6, 9]
giorno: int = int(input("inserisci un giorno da controllare: "))
mese: int = int(input("inserisci il mese da controllare: "))

'''while True:



    if mese in mesi30 and 0 < giorno <= 30:
        break
    elif mese == 2 and 0 < giorno <= 28:
        break
    elif 0 < mese < 13 and mese not in mesi30 and 0 < giorno <= 31:
        break
    else:
        print("Data inserita non corretta")'''

data: tuple[int] = (giorno, mese)

match data:
    case data if mese == 2 and giorno < 1 or giorno > 28:
        print("Data non valida")
    case data if (giorno > 30 or giorno < 1) and mese in mesi30:
        print("Data non valida")
    case data if (giorno > 31 or giorno < 1) or mese < 1 or mese > 12:
        print("Data non valida")
    case(1,1):
        print("Auguri è Capodanno")
    case(30, 3):
        print("Auguri a me, è il mio compleanno")
    case(25, 4):
        print("Auguri è la festa della Liberazione")
    case(25, 12):
        print("Auguri è Natale")
    case(8, 12):
        print("Auguri è l'Immacolata")
    case _:
        print("Festività non trovata, o data non corretta")

