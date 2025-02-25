'''Esercizio 9
Il valore di π può essere approssimato utilizzando la seguente serie infinita:

π = 4 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 + ...

Scrivere un programma che calcoli il valore di π utilizzando questa serie e determini 
quanti termini sono necessari per ottenere approssimazioni sempre più accurate. Quindi:

-progettare un algoritmo che mostri in output quanti termini della serie devono essere usati 
per ottenere il valore di π ≈ 3.14;
-modificare l'algoritmo, mostrando in output quanti termini della serie devono essere usati 
per ottenere il valore di π ≈ 3.141;
-modificare l'algoritmo, mostrando in output quanti termini della serie devono essere usati 
per ottenere il valore di π ≈ 3.1415;
-modificare l'algoritmo, mostrando in output quanti termini della serie devono essere usati 
per ottenere il valore di π ≈ 3.14159.

Nota: Il programma deve iterare fino a raggiungere ciascuna delle soglie indicate, contando 
il numero di termini necessari.'''


i = 2
div:int = 3
pigreco:float = 4
approx:float = 3.141

while True:
    if i % 2 == 0:
        pigreco -= 4 / div
    else:
        pigreco += 4 / div
    if round(pigreco, 3) == approx:
        print(f"\nsono stati necessari {i} termini della serie per arrivare all'approssimazione\n")
        break
    i += 1
    div += 2
    