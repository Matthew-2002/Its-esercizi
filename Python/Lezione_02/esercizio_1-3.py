'''1-3. Si scriva un programma che 
legge tre numeri interi e visualizza la media dei tre numeri.'''


somma = 0
for i in range(3):
    x = int(input('Inserire numero di cui vuoi sapere la media: '))
    somma += x
print(somma/3)