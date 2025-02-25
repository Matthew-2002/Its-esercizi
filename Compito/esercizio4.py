'''Esercizio 4
Scrivere un programma che consenta all'utente di inserire una sequenza di numeri reali 
non negativi (sia interi che decimali). L'inserimento termina quando viene fornito un numero 
negativo, che funge da sentinella e non deve essere considerato nei calcoli.

Il programma deve:

-Calcolare la media dei soli numeri interi inseriti. Utilizzate la funzione is_integer() per 
verificare se il numero inserito è un intero.
-Determinare e visualizzare il numero più grande e il numero più piccolo tra tutti quelli 
inseriti (sia interi che decimali).'''


i:int = 0
m:int = 0
count:int = 0
media:int = 0
Max = 0
Min = 0

while True:
    n = float(input("inserire un numero: (negativo per uscire):\n"))
    
    # imposto la condizione di interruzione del ciclo n < 0
    if n < 0:
        break  
    else:
        
	# alla prima iterazione assegno a massimo e minimo il primo valore n
        if i == 0:
            Min = n
            Max = n 
        
	# confornto n con il massimo e il minimo dalla seconda iterazione
        else:
            if Min > n:
                 Min = n 
            elif Max < n:
                Max = n
        
	# controllo se n è intero e lo calcolo nella media
        if n.is_integer():
            count += n 
            m += 1
            media = count / m
        i += 1

print (f"La media dei numeri interi è: {media}, il numero massimo e il minimo tra i numeri inseriti sono: {Max}, {Min}")