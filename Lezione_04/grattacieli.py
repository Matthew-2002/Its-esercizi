import random;

def campoDiGioco():

    campo: list[int] = []  
    dim: int = int(input("\
scegliere la dimensione del campo di gioco\
(es: 5, per un campo 5x5): "))
   
    for i in range(dim+2):
        riga: list[int] = []
        for y in range(dim+2):
            riga.append(0)
        campo.append(riga)
    
    return campo

def inserimentoQuote(campo):

    inserimento: str = input("Inserisci le quote laterali \
(0xn per prima riga, nx0 per prima colonna, \
(dim+1)xn per ultima riga, \
nx(dim+1) per ultima colonna)\
, 'fine' per terminare: ")

    while inserimento != 'fine':

        riga: int = int(inserimento[0])
        colonna: int = int(inserimento[2])
        valore: int = int(inserimento[-1])

        campo[riga][colonna] = valore

        inserimento: str = input("Inserisci le quote laterali \
(0xn per prima riga, nx0 per prima colonna, \
(dim+1)xn per ultima riga, \
nx(dim+1) per ultima colonna)\
, 'fine' per terminare: ")
    return campo

def check(campo: list[list]):

    check: bool = True
    i: int = 0
    
    for riga in range(len(campo)):
        for col in range(len(campo)):
            
            #se mi trovo sui bordi ma non sugli angoli
            if (riga == 0 or riga == len(campo) - 1)\
            and (col == 0 or col == len(campo) - 1)\
            and not((riga == 0 or riga == len(campo)-1) \
            and (col == 0 or col == len(campo) - 1)):
                
                if campo[riga][col] == 0:
                    continue
                else:

            
                    devoVedere: int = campo[riga][col]
                    if devoVedere == 0:
                        continue
                    else:
                        match (riga, col):

                            case (0, _):

                                visti: int = 0
                                piualto: int = 0
                                for i in range(1, len(campo)-1):
                                    if campo[i][col] == 0:
                                        continue
                                    elif piualto == 0:
                                        piualto = campo[i][col]
                                        visti += 1
                                    elif campo[i][col] > piualto:
                                        piualto = campo[i][col]
                                        visti += 1
                                    if visti > devoVedere:
                                        check = False
                                        return check

                            case (l, _) if l == len(campo) - 1:

                                visti: int = 0
                                piualto: int = 0
                                for i in range(len(campo)-2, 0, -1):
                                    if campo[i][col] == 0:
                                        continue
                                    elif piualto == 0:
                                        piualto = campo[i][col]
                                        visti += 1
                                    elif campo[i][col] > piualto:
                                        piualto = campo[i][col]
                                        visti += 1
                                    if visti > devoVedere:
                                        check = False
                                        return check

                            case (_ , 0):

                                visti: int = 0
                                piualto: int = 0
                                for i in range(1, len(campo)-1):
                                    if campo[riga][i] == 0:
                                        continue
                                    elif piualto == 0:
                                        piualto = campo[riga][i]
                                        visti += 1
                                    elif campo[riga][i] > piualto:
                                        piualto = campo[riga][i]
                                        visti += 1
                                    if visti > devoVedere:
                                        check = False
                                        return check

                            case (_ , l) if l == len(campo) - 1:

                                visti: int = 0
                                piualto: int = 0
                                for i in range(len(campo)-2, 0, -1):
                                    if campo[riga][i] == 0:
                                        continue
                                    elif piualto == 0:
                                        piualto = campo[riga][i]
                                        visti += 1
                                    elif campo[riga][i] > piualto:
                                        piualto = campo[riga][i]
                                        visti += 1
                                    if visti > devoVedere:
                                        check = False
                                        return check
        return check


def tentativi(campo, riga=1, col=1):

    N: int = len(campo) -2

    if riga > N:
        return True
    
    next_riga = riga
    next_col = col + 1
    if next_col > N:
        next_col = 1
        next_riga += 1
    
    if campo[riga][col] != 0:
        return tentativi(campo, next_riga, next_col)
    
    possibili: list[int] = [n for n in range(1, N+1)]
                
    #controllo i numeri possibili
    for i in range(len(campo)):
        if campo[i][col] in possibili:
            possibili.remove(campo[i][col])
        if campo[riga][i] in possibili:
            possibili.remove(campo[riga][i])

    for item in possibili:
        campo[riga][col] = item
        if check(campo):
            if tentativi(campo, next_riga, next_col):
                return True
        campo[riga][col] = 0


'''campo = campoDiGioco()
campo = inserimentoQuote(campo)'''
campo = [
    [0,  0,  3,  0,  2,  0,  0],  # top (parziali)
    [3,  2,  5,  1,  4,  3,  0],  # left + riga 1 + right (0 = nessuna quota)
    [0,  1,  4,  3,  5,  2,  2],
    [2,  4,  2,  5,  3,  1,  0],
    [0,  5,  3,  2,  1,  4,  3],
    [1,  3,  1,  4,  2,  5,  0],
    [0,  0,  2,  0,  3,  0,  0]   # bottom (parziali)
]
if tentativi(campo):
    print("Campo risolto:")
    print(campo)
else:
    print("Nessuna soluzione trovata.")


            







'''x: bool = True

def azzera(campo) -> list[list]:
    for riga in campo:
        for col in campo:
            campo[riga][col]=0
    
    return campo

def solve(campo, riga, col, num) -> list[list]:
    nuovo = [[]]
    numeri = [1,2,3,4,5]
    while x:
        for riga in campo:
            for col in campo:
                for num in random(numeri):
                    if num not in campo[riga]:
                        campo[riga][col]= num
                        numeri.remove(num)
                        if not check(campo[riga][col]):
                            nuovo = azzera(campo)
                            solve(nuovo, riga, col, num)
                        
        x=False

    return nuovo'''
    


                    




                    
                




                

                    
                    













