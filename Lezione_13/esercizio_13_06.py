'''Esercizio 6.

Una produttoria è definita come il prodotto di un 
certo numero n di fattori, con n intero positivo. 
Sia Pi una produttoria definita come segue:
Pi = (0 + 2) * (1 + 2) * (2 + 2) * ... * (2 + n).  

Calcolare il valore della produttoria Pi se n = 7.
'''


def produttoria(n):
    if n == 0:
        return (n+2)
    return produttoria(n-1) * (n+2)

print(produttoria(7))