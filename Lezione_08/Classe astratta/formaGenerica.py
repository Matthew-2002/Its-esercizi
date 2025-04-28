from abc import ABC, abstractmethod

class FormaGenerica(ABC):

    @abstractmethod
    def draw(self) -> None:
        pass

shape: FormaGenerica = FormaGenerica()