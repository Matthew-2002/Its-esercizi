'''Esercizio 3
Scrivere un programma che acquisisca una stringa inserita dall'utente e generi 
una nuova stringa che corrisponda alla versione invertita della stringa originale. 
Il programma deve poi visualizzare la stringa ottenuta in output. Per risolvere 
il problema non si deve utilizzare alcun tipo di funzione, ma esclusivamente i cicli.'''


stringa:str = input("inserisci caratteri da ribaltare:")
stringa_ribaltata:str = ""

for item in stringa:
    stringa_ribaltata = item + stringa_ribaltata
print(stringa_ribaltata)