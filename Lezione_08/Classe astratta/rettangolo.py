from formaGenerica import FormaGenerica

class Rettangolo(FormaGenerica):

    def __init__(self):
        super().__init__()
        
        self.setShape("Rettangolo")

    def draw(self) -> None:
        i = 5
        j = 10    
        for i_ in range(i):
            for j_ in range(j):
                if i_ == 0 or i_ == i-1:
                    print('*', end= "")
                else:
                    if j_ == 0 or j_ == j-1:
                        print("*")

                

rett: Rettangolo = Rettangolo()

rett.draw()