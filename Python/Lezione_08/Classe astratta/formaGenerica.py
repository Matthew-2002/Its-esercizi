from abc import ABC, abstractmethod

class FormaGenerica(ABC):

    @abstractmethod
    def draw(self) -> None:
        pass

    def setShape(self, shape: str) -> None:
        if shape:
            self.shape = shape
        else:
            print("Errore")

    def getShape(self):
        return self.shape
    

#shape: FormaGenerica = FormaGenerica()