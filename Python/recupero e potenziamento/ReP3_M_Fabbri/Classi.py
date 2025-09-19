from typing import Self
import random

class Creatura:

    _nome: str

    def __init__(self, nome: str) -> Self:

        self.set_nome(nome)

    def nome(self) -> Self:

        return self._nome
    
    def set_nome(self, nome: str) -> None:

        if nome.replace(' ', ''):
            self._nome = nome

        else:
            raise ValueError('Il nome non può essere vuoto')
        
    def __str__(self) -> str:

        return f"Creatura: {self.nome()}"
    
class Alieno(Creatura):

    _matricola: int
    _munizioni: list[int]

    def __init__(self, nome: str) -> Self:
 
        self.__set_matricola()
        self.__set_munizioni()        
        
        if nome[:6] == 'Robot-':
            super().__init__(nome)
            self._nome = nome + str(self._matricola)
        else:
            print("Attenzione! Tutti gli Alieni devono avere \
il nome 'Robot-' seguito dal numero di matricola! Reimpostazione \
nome Alieno in Corso!")
            raise KeyError


    def __set_matricola(self) -> None:

        matricola: int = random.randint(10000, 90000)
        self._matricola = matricola

    def __set_munizioni(self) -> None:

        munizioni: list[int] = [i*i for i in range(15) if i%2==1 or i==0]
        self._munizioni = munizioni
    
    def __str__(self) -> str:

        if self._nome:

            return f"Alieno: {self._nome}"


a: Alieno = Alieno('Robot-')
print(a)

class Mostro(Creatura):

    urlo_vittoria: str
    gemito_sconfitta: str
    assalto: list[int]

    def __init__(self, nome:str, urlo_vittoria: str, 
                 gemito_sconfitta: str) -> Self:

        super().__init__(nome)
        self.__set_vittoria(urlo_vittoria)
        self.__set_sconfitta(gemito_sconfitta)
        self.__set_assalto()


    def __set_vittoria(self, urlo_vittoria: str) -> None:

        if urlo_vittoria.replace(' ', '') \
        and type(urlo_vittoria) == 'str':
            
            self._urlo_vittoria = urlo_vittoria

        else:

            self._urlo_vittoria = 'GRAAAHHH'
            
    def __set_sconfitta(self, gemito_sconfitta: str) -> None:

        if gemito_sconfitta.replace(' ', '') \
        and type(gemito_sconfitta) == 'str':
            
            self._gemito_sconfitta = gemito_sconfitta

        else:

            self._gemito_sconfitta = 'Uuurghhh'

    def __set_assalto(self) -> None:

        self._assalto = []
        while len(self._assalto) < 15:
            n = random.randint(1,100)
            if n not in self._assalto:
                self._assalto.append(n)

    def __str__(self) -> str:

        nuovo_nome: str = ''
        i=0
        for item in self._nome:
            if i % 2 == 0:
                nuovo_nome += item.upper()
            else:
                nuovo_nome += item.lower()
            i += 1
        return f'{nuovo_nome}'

    def urlo_vittoria(self) -> str:

        return self._urlo_vittoria
    
    def gemito_sconfitta(self) -> str:

        return self._gemito_sconfitta
    
    def assalto(self) -> list[int]:

        return self._assalto

m: Mostro = Mostro('Bella', "", "")
print(m, m.assalto(), m.gemito_sconfitta(), m.urlo_vittoria())