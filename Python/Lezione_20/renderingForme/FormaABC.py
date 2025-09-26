from abc import ABC, abstractmethod

class Forma(ABC):
     
    def __init__(self,
    ) -> None:
        self.forma = ''

    @abstractmethod
    def getArea(self) -> None:
        pass

    @abstractmethod
    def render(self) -> None:
        pass

