'''Esercizio 8
Un'applicazione interessante dei computer è la rappresentazione grafica di dati.
Scrivere un programma che acquisisca cinque numeri interi (ognuno compreso tra 1 e 30) 
e visualizzi in output un grafico a barre testuale con asterischi *.

Per ogni numero letto, il programma deve stampare una riga contenente tanti asterischi 
quanti il valore del numero stesso.

Esempio di output:
Se l'utente inserisce i numeri 5, 8, 3, 12, 7, il programma deve stampare:

*****
********
***
************
*******
'''

numero_1:int = int(input("inserisci il primo numero"))
numero_2:int = int(input("inserisci il secondo numero"))
numero_3:int = int(input("inserisci il terzo numero"))
numero_4:int = int(input("inserisci il quarto numero"))
numero_5:int = int(input("inserisci il quinto numero"))

lista:list[int] = [numero_1, numero_2, numero_3, numero_4, numero_5]
asterischi:list[str] = []

# inizializzo il contatore, imposto il ciclo per ogni numero nella lista e lo controllo

for item in lista:
    if item > 30 or item < 1:
        print (f"I numeri devono essere compresi tra 1 e 30")
        break
    
    # imposto un altro ciclo per aggiungere asterischi in una lista tanti quanti il valore del numero
    else:
        i = 0
        while i < item:
            asterischi.append("*")
            
	    # prima che esca dal ciclo stampo gli asterichi e cancello gli elementi della lista
            if i == (item-1):
                print(''.join(asterischi))
                del asterischi[:]
            i += 1