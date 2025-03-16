
import math


def numero_primo(n):
    if n <= 1:
        return False
    else:
        Div = 2
        while Div <= math.sqrt(n):
            if n % Div == 0:
                return False
            else:
                Div += 1
        return True

def scomposizione(n): 
    numero:int = n
    Div2 = 2
    primi: dict[int, int] = {}
    
    if numero_primo(n) == True:
        return False
   
    while numero_primo(numero) == False:
       
        if numero % Div2 == 0:
            if Div2 in primi:
                primi[Div2] += 1
            else:    
                primi[Div2] = 1
            numero /= Div2
        else:
            Div2 += 1

    if numero in primi:
        primi[numero] += 1
    else:
        primi[numero] = 1
    return primi

primi:dict[int] = scomposizione(int(input("Inserisci numero da scomporre in afttori primi: ")))

if primi == False:
    print("Il numero inserito si può dividere solo per se stesso")
else:
    print("Il tuo numero è composto da: ", end= "")
    for key,value in primi.items():
        print(f"{key} elevato {value} volte", end= ", ")