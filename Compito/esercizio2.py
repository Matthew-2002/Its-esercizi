'''Esercizio 2
Scrivere un programma che acquisisca una stringa inserita dall'utente e calcoli 
il numero totale di spazi presenti nella stringa. Il risultato deve essere 
visualizzato in output.'''

stringa:str = input("inserisci il testo di cui vuoi conoscere il numero di spaziature:")

count = 0
for item in stringa:
    if item == " ":
        count += 1
print(f"il numero toatale di spaziature è: {count}")