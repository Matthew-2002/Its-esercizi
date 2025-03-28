import random

posizione_t: int = 0
posizione_l: int = 0

def posizione_gara(posizione_t, posizione_l):
    
    #creo il percorso
    percorso: list[any] = []
    for i in range(1,71):
        percorso.append("_")

    #evito list index out of range        
    if posizione_t >= len(percorso):
        posizione_t = len(percorso) -1
    if posizione_l >= len(percorso):
        posizione_l = len(percorso) -1
    
    #inserisco "L" e "T" nel percorso e stampo
    if posizione_t == posizione_l == len(percorso)-1:
        print("OUCH!!!")
        percorso[posizione_t] = "T"
        percorso[posizione_l-1] =  "L"
    elif posizione_t == posizione_l:
        print("OUCH!!!")
        percorso[posizione_t+1] = "T"
        percorso[posizione_l] =  "L"
    else:
        percorso[posizione_t] =  "T"
        percorso[posizione_l] =  "L"
    print("".join(percorso))

def mossa_t(n, posizione_t, meteo, energia):
    
    #percentuali mosse con meteo soleggiato
    if meteo == 'soleggiato':   
        
        #passo veloce
        if 1 <= n <= 50:
            if energia >= 5:
                posizione_t += 3
                energia -= 5
            else:
                energia += 10
        #passo lento
        elif 51 <= n <= 80:
            if energia >= 3:
                posizione_t += 1
                energia -= 3
            else:
                energia += 10
        #scivolata
        else:
            if energia >= 10:
                posizione_t -= 6
                energia -=10
            else:
                energia += 10
        if posizione_t < 1:
            posizione_t = 1
        return posizione_t
    
    #percentuali mosse con meteo piovoso
    if meteo == 'piovoso':
        
        #passo veloce
        if 1 <= n <= 45:
            if energia >= 5:    
                posizione_t += 3
                energia -= 5
            else:
                energia += 10
        #passo lento
        elif 46 <= n <= 70:
            if energia >= 3:    
                posizione_t += 1
                energia -= 3
            else:
                energia += 10
        #scivolata
        else:
            if energia >= 10:
                posizione_t -= 6
                energia -= 10
            else:
                energia += 10
        if posizione_t < 1:
            posizione_t = 1
        return posizione_t

def mossa_l(n, posizione_l, meteo, energia):
    
    #percentuali mosse con meteo soleggiato  
    if meteo == 'soleggiato':
        
        #grande balzo
        if 1 <= n <= 20:
            if energia >= 15:    
                posizione_l += 9
                energia -= 15
            else:
                energia += 10
        #piccolo balzo
        elif 21 <= n <= 50:
            if energia >= 5:
                posizione_l += 1
                energia -= 5
            else:
                energia += 10
        #piccola scivolata
        elif 51 <= n <= 70:
            if energia >= 8:
                posizione_l -= 2
                energia -= 8
            else:
                energia += 10
        #grande scivolata
        elif 71 <= n <= 80:
            if energia >= 20:
                posizione_l -= 12
                energia -= 20
            else:
                energia += 10      
        if posizione_l < 1:
            posizione_l = 1
        return posizione_l
    
    #percentuali mosse con meteo soleggiato    
    if meteo == 'piovoso':
        
        #grande balzo
        if 1 <= n <= 17:
            if energia >= 15:    
                posizione_l += 9
                energia -= 15
            else:
                energia += 10
        #piccolo balzo
        elif 18 <= n <= 44:
            if energia >= 5:
                posizione_l += 1
                energia -= 5
            else:
                energia += 10
        #piccola scivolata
        elif 45 <= n <= 70:
            if energia >= 8:
                posizione_l -= 2
                energia -= 8
            else:
                energia += 10
        #grande scivolata
        elif 71 <= n <= 83:
            if energia >= 20:
                posizione_l -= 12
                energia -= 20
            else:
                energia += 10
        
        if posizione_l < 1:
            posizione_l = 1
        return posizione_l

#inizia la gara
print("BANG !!!!! AND THEY'RE OFF !!!!!")
posizione_gara(posizione_t, posizione_l)
energia_l: int = 100
energia_t: int = 100

i: int = 0
while (posizione_l < 70 and posizione_t < 70) and (energia_t > 0 or energia_l > 0):
    
    #inserisco le condizioni variabili ogni 10 tick
    if (i // 10) % 2 == 0:
        meteo: str = 'soleggiato'
    else:
        meteo: str = 'piovoso'

    #assegno le mosse richiamando funzioni
    posizione_l = mossa_l((random.randint(1, 100)), posizione_l, meteo, energia_l)
    posizione_t = mossa_t((random.randint(1, 100)), posizione_t, meteo, energia_t)
    posizione_gara(posizione_t, posizione_l)
    i += 1

#controllo il vincitore
if posizione_t == 70 and posizione_l == 70:
    print("TORTOISE WINS! || VAY!!!")
elif posizione_t >= 70:
    print("TORTOISE WINS! || VAY!!!")
else:
    print("HARE WINS || YUCH!!!")
if energia_l == energia_t == 0:
    print("Animals are tired, race ended!!!")