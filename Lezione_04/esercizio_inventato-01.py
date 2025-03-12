
import math


def numero_primo(n):
    if n == 1:
        return("il numero 1 non è primo")
    elif n < 1:
        return("Il numero è 0 o negativo")
    else:
        Div = 2
        while Div <= math.sqrt(n):
            if n % Div == 0:
                return("il numero non è primo")
                break
            Div += 1
        else:
            return("il numero è primo")


def scomposizione(n):
    numero:int = n
    i=2
    if numero_primo(numero) == "il numero è primo":
        return(f"Il numero {n} si può scomporre come {n}**1")
    while numero_primo(numero) == "il numero non è primo":
        if numero % i == 0:
            if i in primi:
                primi[i] += 1
            else:
                primi[i] = 1
            i = 1
            numero /= i
        i += 1
    if numero in primi:
        primi[numero] += 1
    else:
        primi[numero] = 1
    return primi
n = int(input("Inserisci il numero di cui vuoi sapere la scomposizione in fattori primi: "))
primi: dict[int, int] = {}
print(scomposizione(n))
