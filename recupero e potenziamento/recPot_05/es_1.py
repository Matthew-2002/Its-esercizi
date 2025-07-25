'''1.A Scrivere una funzione genera() che data in input la dimensione 
dim della matrice genera una matrice quadrata di dimensione dim x dim, 
ovvero una matrice che ha dim righe e dim colonne. Ogni elemento di 
questa matrice è un numero random tra 0 e 13. Inoltre, in ogni riga, 
ogni elemento della riga deve essere diverso dal primo elemento della 
riga stessa.'''

import random

def genera(dim: int) -> list[list[int]]:

    mat:list[list] = []
    
    for r in range(dim):
    
        riga: list[int] = []
    
        for c in range(dim):

            while True:

                n: int = random.randint(0, 13)

                if c == 0:

                    riga.append(n)
                    break
                
                else:

                    if riga[0] != n:

                        riga.append(n)
                        break
        mat.append(riga)

    return mat


def calcolaCarico(mat, r, c) -> int:

    carico: int = 0
    
    for i in range(len(mat)):
        carico += mat[r][i]
        carico -= mat[i][c]

    return carico


def printMAT(mat) -> None:

    print()

    for r in range(len(mat)):

        for c in range(len(mat)):

            
            print(f'{str(mat[r][c]).center(5)}', end= '')
        
        print(f'\n')


def caricoNullo(mat) -> list[tuple[int, int]]:

    carichiNulli:list[tuple[int, int]] = []
    
    for r in range(len(mat)):

        for c in range(len(mat)):

            carico:int = calcolaCarico(mat, r, c)
           
            if carico == 0:

                carichiNulli.append((r, c))
    
    return carichiNulli


def caricoMAX(mat) -> tuple[int]:

    for r in range(len(mat)):

        for c in range(len(mat)):

            carico:int = calcolaCarico(mat, r, c)
            
            if r == 0 and c == 0:

                caricomax = carico
                indici: tuple = (r, c)
            
            else:

                if carico > caricomax:

                    caricomax = carico
                    indici: tuple = (r, c)
    
    print(caricomax)
    return indici

def caricoMIN(mat) -> tuple[int]:

    for r in range(len(mat)):

        for c in range(len(mat)):

            carico:int = calcolaCarico(mat, r, c)
            
            if r == 0 and c == 0:

                caricomin = carico
                indici: tuple = (r, c)
            
            else:

                if carico < caricomin:

                    caricomin = carico
                    indici: tuple = (r, c)
    
    print(caricomin)
    return indici




mat = genera(5)
printMAT(mat)

print(caricoNullo(mat))

rmax, cmax = caricoMAX(mat)
caricoMAX(mat)
print(rmax, cmax)
print(calcolaCarico(mat, rmax, cmax))

rmin, cmin = caricoMIN(mat)
caricoMIN(mat)
print(rmin, cmin)
print(calcolaCarico(mat, rmin, cmin))






                        