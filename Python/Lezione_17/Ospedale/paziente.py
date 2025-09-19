from typing import Self
from persona import Persona

class Paziente(Persona):

    __first_name: str | None
    __last_name: str | None
    __age: int | None
    __idCode: str | None   

    def __init__(self,
        first_name: str|None,
        last_name: str|None,
        idCode: str
    ) -> Self:
        super().__init__(
            first_name,
            last_name
        )
        if idCode == str:
            self.__idCode = idCode
        else:
            self.__idCode = None
            print('Codice ID invalido')
    
    def setIdCode(self,
        idCode: str
    ) -> None:
        if idCode == str:
            self.__idCode = idCode
        else:
            self.__idCode = None
            print('Codice ID invalido')

    def getIdCode(self) -> str|None:
        return self.__idCode
    
    def patientInfo(self) -> str:
        print(f'Paziente: {self.__first_name} {self.__last_name}\n\
ID {self.__idCode}')
        