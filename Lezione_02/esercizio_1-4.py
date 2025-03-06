'''
1-4. Si scriva un programma che dato un intero di quattro cifre, 
per esempio 2024, utilizzando gli opportuni operatori, lo si visualizzi, 
una cifra per riga:

2
0
2
4
'''

n: int = int(input("Inserire numero di 4 cifre:"))
m: int = n // 1000
c: int = n // 100 - m * 10
d: int = n // 10 - m * 100 - c * 10
u: int = n - m * 1000 - c * 100 - d * 10

print (m)
print (c)
print (d)
print (u)