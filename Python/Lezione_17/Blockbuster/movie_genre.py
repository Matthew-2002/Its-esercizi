from typing import Self
from film import Film

class Azione(Film):

    __genere: str
    __penale: float

    def __init__(self,
        id,
        title
    ) -> Self:
        super().__init__(id, title)
        self.__genere = 'Azione'
        self.__penale = 3.00

    def getGenere(self) -> str:
        return self.__genere
    
    def getPenale(self) -> float:
        return self.__penale
    
    def calcolaPenaleRitardo(self,
        n_giorni
    ) -> float:
        return n_giorni * self.getPenale()
    

class Commedia(Film):

    __genere: str
    __penale: float

    def __init__(self,
        id,
        title
    ) -> Self:
        super().__init__(id, title)
        self.__genere = 'Commedia'
        self.__penale = 2.50

    def getGenere(self) -> str:
        return self.__genere
    
    def getPenale(self) -> float:
        return self.__penale
    
    def calcolaPenaleRitardo(self,
        n_giorni
    ) -> float:
        return n_giorni * self.getPenale()
    

class Drama(Film):

    __genere: str
    __penale: float

    def __init__(self,
        id,
        title
    ) -> Self:
        super().__init__(id, title)
        self.__genere = 'Drama'
        self.__penale = 2.00

    def getGenere(self) -> str:
        return self.__genere
    
    def getPenale(self) -> float:
        return self.__penale
    
    def calcolaPenaleRitardo(self,
        n_giorni
    ) -> float:
        return n_giorni * self.getPenale()
    

