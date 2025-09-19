from typing import Self

class Persona:

    __first_name: str|None
    __last_name: str|None
    __age: int|None

    def __init__(self,
        first_name: str|None,
        last_name: str|None
    ) -> Self:
        if type(first_name) == str and type(last_name) == str:
            self.__first_name = first_name
            self.__last_name = last_name
            self.__age = 0
        else:
            self.__first_name = None
            self.__last_name = None
            self.__age = None
            if type(first_name) != str:
                print('Il nome non è una stringa')
            if type(last_name) != str:
                print('Il cognome non è una stringa')
    
    def setFirstName(self,
        first_name: str
    ) -> None:
        if type(first_name) == str:
            self.__first_name = first_name
        else:
            self.__first_name = None
            print('Il nome non è una stringa')
    
    def setLastName(self,
        last_name: str
    ) -> None:
        if type(last_name) == str:
            self.__last_name = last_name
        else:
            self.__last_name = None
            print('Il cognome non è una stringa')
    
    def setAge(self,
        age: int
    ) -> None:
        if type(age) == int:
            self.__age = age
        else:
            self.__age = None
            print('L\'età non è un intero')

    def getFirstName(self) -> str:
        return self.__first_name
    
    def getLasstName(self) -> str:
        return self.__last_name
    
    def getAge(self) -> str:
        return self.__age
    
    def greet(self) -> str:
        print(f'\"Ciao sono {self.__first_name} {self.__last_name}! \
Ho {self.__age} anni!\"')
        
    
 



