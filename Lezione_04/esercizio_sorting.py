from datetime import datetime

def sorting(lista: list[int]): 

    ordered: bool = True
    
    for x in range(len(lista)):

        indice_min = x
        min_: int = lista[x]

        for y in range(x, len(lista)):           
            
            if min_ > lista[y]:
                min_ = lista[y]
                indice_min = y

        if indice_min != x:
            lista[indice_min] = lista[x]
            lista[x] = min_

    
    return lista


'''print(sorting([1,5,3,6,4,14324,4545,6,7,54,3,6,767,65,5]))'''


class clock():

    def __enter__(self):

        self.inizio = datetime.now()

    def __exit__(self, exc_type, exc_value, traceback):

        self.fine = datetime.now()
        durata = self.fine - self.inizio
        print(f"il programma ha impiegato {durata} secondi")

with clock():

    print(sorting([1,5,3,6,4,14324,4545,6,7,54,3,6,767,65,5,1]))