from typing import Self
from persona import Persona

class Dottore(Persona):

    __first_name: str|None
    __last_name: str|None
    __age: int|None
    __specialization: str|None
    __parcel: float|None

    def __init__(self,
        first_name: str|None,
        last_name: str|None,
        specialization: str,
        parcel: float
    ) -> Self:
        super().__init__(
            first_name,
            last_name,
            )
        if type(specialization) == str:
            self.__specialization = specialization
        else:
            self.__specialization = None
            print('La specializzazione inserita non è valida')

        if type(parcel) == float:
            self.__parcel = parcel
        else:
            self.__parcel = None
            print('La parcella inserita non è valida')
    
    def setSpecialization(self,
        specialization: str
    ) -> None:
        if type(specialization) == str:
            self.__specialization = specialization
        else:
            self.__specialization = None
            print('La specializzazione inserita non è valida')
    
    def setParcel(self,
        parcel: float
    ) -> None:
        if type(parcel) == float:
            self.__parcel = parcel
        else:
            self.__parcel = None
            print('La parcella inserita non è valida')
    
    def getSpecialization(self) -> str|None:
        return self.__specialization
    
    def getParcel(self) -> float|None:
        return self.__parcel
    
    def isAValidDoctor(self) -> str:
        if self.__age > 30:
            print(f'Doctor {self.__first_name} {self.__last_name} is valid')
            return True
        else:
            print(f'Doctor {self.__first_name} {self.__last_name} is not valid')
            return False
    
    def doctorGreet(self) -> str:
        super().greet()
        print(f'Sono un medico {self.__specialization}')
