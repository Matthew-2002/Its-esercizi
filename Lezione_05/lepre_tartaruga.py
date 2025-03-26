import random

percorso: list[any] = []
posizione_t: int = 1
posizione_l: int = 1

def posizione_gara(posizione_t, posizione_l):
    percorso: list[any] = []
    for i in range(1, 73):
        percorso.append("_")    
    if posizione_t-1 >= len(percorso):
        posizione_t = len(percorso)
    elif posizione_l-1 >= len(percorso):
        posizione_l = len(percorso)
    else:    
        if posizione_t == posizione_l:
            print("OUCH!!!")
            percorso[posizione_t] = "T"
            percorso[posizione_l-1] =  "L"
        else:
            percorso[posizione_t-1] =  "T"
            percorso[posizione_l-1] =  "L"
        print("".join(percorso))

def mossa_t(n, posizione_t, meteo):
    if meteo == 'soleggiato':   
        if 1 <= n <= 50:
            posizione_t += 3
        elif 51 <= n <= 80:
            posizione_t += 1
        else:
            posizione_t -= 6
            if posizione_t < 1:
                posizione_t = 1
        return posizione_t
    if meteo == 'piovoso':
        if 1 <= n <= 45:
            posizione_t += 3
        elif 46 <= n <= 70:
            posizione_t += 1
        else:
            posizione_t -= 6
        posizione_t -= 1
        if posizione_t < 1:
            posizione_t = 1
        return posizione_t

def mossa_l(n, posizione_l, meteo):
    if meteo == 'soleggiato':
        if 1 <= n <= 20:
            posizione_l += 9
        elif 21 <= n <= 50:
            posizione_l += 1
        elif 51 <= n <= 70:
            posizione_l -= 2
        elif 71 <= n <= 80:
            posizione_l -= 12        
        if posizione_l < 1:
            posizione_l = 1
        return posizione_l
    if meteo == 'piovoso':
        if 1 <= n <= 17:
            posizione_l += 9
        elif 18 <= n <= 44:
            posizione_l += 1
        elif 45 <= n <= 70:
            posizione_l -= 2
        elif 71 <= n <= 83:
            posizione_l -= 12        
        posizione_l -= 2
        if posizione_l < 1:
            posizione_l = 1
        return posizione_l

print("BANG !!!!! AND THEY'RE OFF !!!!!")
posizione_gara(posizione_t, posizione_l)

i: int = 0
while posizione_l < 71 and posizione_t < 71:
    
    if (i // 10) % 2 == 0:
        meteo: str = 'soleggiato'
    else:
        meteo: str = 'piovoso'
    posizione_l = mossa_l((random.randint(1, 100)), posizione_l, meteo)
    posizione_t = mossa_t((random.randint(1, 100)), posizione_t, meteo)
    posizione_gara(posizione_t, posizione_l)
    i += 1

if posizione_t > 72 and posizione_l > 72:
    print("TORTOISE WINS! || VAY!!!")
elif posizione_t > 70:
    print("TORTOISE WINS! || VAY!!!")
else:
    print("HARE WINS || YUCH!!!")