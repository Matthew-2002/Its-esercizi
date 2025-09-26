from FormaABC import Forma

class Quadrato(Forma):

    def __init__(self,
        lato
    ) -> None:
        self.lato = lato
        self.forma = 'quadrato'

    def getArea(self) -> float:
        return self.lato*2
    
    def render(self) -> str:
        for y in range(self.lato):
            for x in range(self.lato):
        #        if y == 0 or y == self.lato-1:
        #            print('*', end= " ")
        #            if x == self.lato-1 and y == 0:
        #                print()
        #        else:
        #            if y == 0:
        #                print("*", " "*(y*2-4), end= "")
        #            elif j_ == j-1:
        #                print("*")

                match (y, x):
                    case (y, x) if (y == 0|self.lato-1) and x != self.lato-1:
                        print('*', end= ' ')
                    case (y, x) if x == self.lato-1:
                        print('*')
                    case (y, 0):
                        print('*', end=' ')
                    case _:
                        print(' ', end=' ')

q = Quadrato(5)
q.render()

                    