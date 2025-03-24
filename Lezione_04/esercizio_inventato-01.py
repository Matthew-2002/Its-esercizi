
import math


def numero_primo(n):
    if n <= 1:
        return False
    else:
        div = 2
        while div <= math.sqrt(n):
            if n % div == 0:
                return False
            else:
                div += 1
        return True

def scomposizione(n): 
    numero:int = n
    div = 2
    primi: dict[int, int] = {}
   
    while numero_primo(numero) == False:
       
        if numero % div == 0:
            if div in primi:
                primi[div] += 1
            else:    
                primi[div] = 1
            numero /= div
        else:
            Div += 1

    if numero in primi:
        primi[int(numero)] += 1
    else:
        primi[int(numero)] = 1
    return primi

primi:dict[int] = scomposizione(int(input("Inserisci numero da scomporre in afttori primi: ")))

if primi == {}:
    print("Il numero inserito si può dividere solo per 1 e per se stesso")
else:
    print("Fattori primi:")
    for key,value in primi.items():
        print(f"    {key} elevato a {value}")