import random

percorso: list[any] = []
posizione_t: int = 1
posizione_l: int = 1

def posizione_gara(posizione_t, posizione_l):
    percorso: list[any] = []
    for i in range(1, 73):
        percorso.append("_")    
    if posizione_t == posizione_l:
        print("OUCH!!!")
        percorso[posizione_t] = "T"
        percorso[posizione_l-1] =  "L"
    else:
        percorso.insert(posizione_t, "T")
        percorso.insert(posizione_l, "L")
    print("".join(percorso))

def mossa_t(n, posizione_t, meteo):
    if meteo == 'soleggiato':   
        if 1 <= n <= 5:
            posizione_t += 3
        elif n == 6 or n == 7:
            posizione_t -= 6
            if posizione_t < 1:
                posizione_t = 1
        else:
            posizione_t += 1
        return posizione_t
    if meteo == 'piovoso':
        if 1 <= n <= 5:
            posizione_t += 3
        elif 6 <= n <= 10:
            posizione_t -= 6
        if posizione_t < 1:
            posizione_t = 1
        else:
            posizione_t += 1
        return posizione_t

def mossa_l(n, posizione_l, meteo):
    if meteo == 'soleggiato':
        if n == 1 or n == 2:
            posizione_l += 9
        elif n == 3:
            posizione_l -= 12
            if posizione_l < 1:
                posizione_l = 1
        elif 4 <= n <= 6:
            posizione_l += 1
        elif n == 7 or n == 8:
            posizione_l -= 2
            if posizione_l < 1:
                posizione_l = 1
        return posizione_l
    if meteo == 'piovoso':
        if n == 1 or n == 2:
            posizione_l += 9
        elif n == 3 or n == 10:
            posizione_l -= 12
            if posizione_l < 1:
                posizione_l = 1
        elif 4 <= n <= 6:
            posizione_l += 1
        elif 7 <= n <= 9:
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
    posizione_l = mossa_l((random.randint(1, 12)), posizione_l, meteo)
    posizione_t = mossa_t((random.randint(1, 12)), posizione_t, meteo)
    posizione_gara(posizione_t, posizione_l)
    i += 1

if posizione_t > 70 and posizione_l > 70:
    print("TORTOISE WINS! || VAY!!!")
elif posizione_t > 70:
    print("TORTOISE WINS! || VAY!!!")
else:
    print("HARE WINS || YUCH!!!")