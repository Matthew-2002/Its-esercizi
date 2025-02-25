'''Esercizio 6
Scrivere un programma che acquisisca in input due numeri interi, n1 e n2, 
e calcoli il prodotto di tutti i numeri compresi tra n1 e n2, inclusi gli estremi.

Il programma deve gestire anche il caso in cui n1 > n2, calcolando comunque il 
prodotto correttamente.'''


n1 = int(input("Inserisci primo numero:"))
n2 = int(input("Inserisci secondo numero:"))
prod = 1

# sviluppo il caso n1 < n2, calcolo il prodotto, incremento n1 di 1 fino a n2
if n1 < n2:
    while n1 <= n2:
        prod *= n1
        n1 += 1 
    print (f"Il prodotto che cercavi è: {prod}")

# sviluppo il caso n2 < n1, calcolo il prodotto, incremento n2 di 1 fino a n1
elif n1 > n2:
    while n2 <= n1:
        prod *= n2
        n2 += 1 
    print (f"Il prodotto che cercavi è: {prod}")

else:
    print (f"I numeri inseriti sono uguali il prodotto che cercavi è {n1}")