'''Esercizio 7
Scrivere un programma che inizializzate due liste a e b della stessa lunghezza n, 
entrambe contenenti valori interi, calcoli la somma incrociata degli elementi.'''


a:list[int] = [1, 6, 7, 10]
b:list[int] = [5, 7, 12, 3]
c:list[int] = []
n:int = 4


for i in range (n):
    c.append(a[i] + b[(- (i+1))])

print(a, b, c)















