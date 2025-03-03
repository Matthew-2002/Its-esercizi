'''Esercizio 3C-7. Si scriva un programma in python che computi 
la statistica di otto lanci di una moneta.
Per ciascuno dei lanci effettuati, l'utente inserisce "t" o "T" 
se è uscito "testa", mentre inserisce "c" o "C" se è uscito "croce".
Il programma deve mostrare in output il numero totale e la 
percentuale dei risultati "testa" e "croce".

NOTA.
Le percentuali devono essere mostrate in output obbligatoriamente 
con 2 cifre decimali.
Usare il match statement.
'''

teste:int = 0
croci:int = 0

while croci + teste < 8:
    lancio:str = input(f"inserisci il risultato del lancio {croci+teste+1}: ").lower()
    match lancio:      
        case "t":
            teste += 1
        case "c":
            croci += 1
        case _:
            print("Lancio non valido, riprovare")

prob:float = (teste/8)*100
print(f"%teste: {prob:.2f}%, %croci : {100-prob:.2f}%")


