'''Esercizio 3C-00B. Scrivere un programma in Python che chieda all'utente di inserire 
il proprio nome e il proprio genere (specificato con "m" per maschio o "f" per femmina) 
e utilizzi lo statement match per fornire una risposta adeguata da inserire in un 
documento di identita'.

- Se il valore di gender è "m", stampare il nome e il genere come Maschio.
- Se il valore di gender è "f", stampare il nome e il genere come Femmina.
- Se il valore di gender è diverso da "m" o "f", stampare un messaggio di 
errore, indicando che non è possibile generare un documento di identità.'''


nome:str = input("Inserisci il tuo nome: ")
gender:str = input("Inserisci il tuo gender (m, f): ")
match gender:
    case "m":
        print(f"Nome: {nome}\nGenere: Maschio")
    case "f":
        print(f"Nome: {nome}\nGenere: Femmina")
    case _:
        print("Non è possibile generare un documento di identità")