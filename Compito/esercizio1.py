'''Esercizio 1
Scrivere un programma che permetta all'utente di inserire una serie di parole in input, 
terminando l'inserimento quando viene digitata la parola "fine" (che non deve essere 
considerata nell'elaborazione).
Per ogni parola inserita, il programma deve verificare se il primo e l'ultimo carattere 
sono uguali e visualizzare un messaggio corrispondente.'''

parola:str = input("inserisci una parola:\n")

while parola != "fine":
    if parola[0] == parola[-1]:
        print("il primo e l'ulitimo carattere inseriti corrispondono")
    else:
        print("Primo e ultimo carattere non corrispondono")
    parola:str = input("inserisci una parola:\n")