from typing import Self

class Film:

    id: int
    title: str

    def __init__(self,
        id: int,
        title: str
    ) -> Self:
        self.__id = id
        self.__title = title
    
    def setId(self,
        id
    ) -> None:
        self.__id = id

    def setTitle(self,
        title
    ) -> None:
        self.__title = title

    def getId(self) -> int:
        return self.__id
    
    def getTitle(self) -> str:
        return self.__title
    
    def isEqual(self,
        id2
    ) -> bool:
        if self.getId() == id2:
            return True
        return False
    

    


        