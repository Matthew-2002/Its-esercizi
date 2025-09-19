'''
14. Sudoku Solver:

    Create a function that solves a Sudoku puzzle 
    using backtracking.
    Provide a 9x9 grid representing the puzzle with 
    some numbers filled in and others left blank.
    Implement a backtracking algorithm to check for 
    valid placements in empty cells, ensuring no row, 
    column, or 3x3 subgrid contains duplicates.
    Solve the puzzle by filling in the remaining empty 
    cells with valid numbers.'''


#creo il campo di gioco
campo: list[str] = [' ' for i in range(81)]
inserimento: str = input("Inserisci numeri \
(es: prima casella --> '1x1 = 5'), 'fine' per terminare: ")
list_inserimento: list[any] = list(inserimento)
while inserimento != 'fine':
    riga: int = int(list_inserimento[0]) - 1
    colonna: int = int(list_inserimento[1]) - 1
    campo[riga*9+colonna] = list_inserimento[-1]
    inserimento: str = input("Inserisci numeri 'fine' per terminare: ")
    list_inserimento: list[any] = list(inserimento)

#controllo semplice sudoku
def controllo_semplice(campo):
    for item in campo:
        if item == " ":
            probabili: list[int] = [1,2,3,4,5,6,7,8,9]
            riga: int = campo.index(item) // 9
            colonna: int = campo.index(item) - riga * 9
            
            #controllo a destra del numero
            for i in range(1, 9 - colonna):
                if campo[campo.index(item) + i] != ' ':
                    if campo[campo.index(item) + i] in probabili:
                        probabili.remove(campo[campo.index(item) + i])
            
            #controllo a sinistra del numero
            for i in range(1, colonna):
                if campo[campo.index(item) - i] != ' ':
                    if campo[campo.index(item) + i] != ' ':
                        probabili.remove(campo[campo.index(item) - i])

            #controllo sopra il numero
            for i in range(1, riga):
                if campo[campo.index(item) - 9*i] != ' ':
                    if campo[campo.index(item) + i] != ' ':
                        probabili.remove(campo[campo.index(item) - 9*i])
            
            #controllo sotto il numero
            for i in range(1, 9 - riga):
                if campo[campo.index(item) + 9*i] != ' ':
                    if campo[campo.index(item) + i] != ' ':
                        probabili.remove(campo[campo.index(item) + 9*i])
            
            #controllo quadrato
            quadrato_elemento: int = colonna // 3 + (riga // 3) * 3
            for item_confronto in campo:
                riga_confronto: int = campo.index(item_confronto) // 9
                colonna_confronto: int = campo.index(item_confronto) - riga * 9
                quadrato_confronto: int = colonna_confronto // 3 + (riga_confronto // 3) * 3
                if quadrato_confronto == quadrato_elemento:
                    if item_confronto != ' ':
                        if campo[campo.index(item) + i] != ' ':
                            probabili.remove(item_confronto)
            
            #scrivo elementi certi
            if len(probabili) == 1:
                item = probabili[0]
            
    return campo

def mostra_campo(campo):
    for i in range(len(campo)):
        if i % 9 == 0:
            print()
        print(campo[i], end= ' ')

while ' ' in campo:
    campo = controllo_semplice(campo)
mostra_campo(campo)


