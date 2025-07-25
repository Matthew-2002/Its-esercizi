from abc import ABC, abstractmethod
from typing import Self
import string

class CodificatoreMessaggio(ABC):

    @abstractmethod
    def codifica(self, 
        testoInChiaro
    ) -> str:
        pass

class DecodificatoreMessaggio(ABC):

    @abstractmethod
    def decodifica(self,
        testo_cifrato
    ) -> str:
        pass

'''    @abstractmethod
    def leggi_file(self,
        path: str
    ) -> str:
        pass

    @abstractmethod
    def scrivi_file(self) -> None:
        pass'''

class CifratoreAScorrimento(
    CodificatoreMessaggio,
    DecodificatoreMessaggio
):
    
    chiave: int

    def __init__(self, 
            chiave: int
        ) -> Self:
        
        self.chiave = chiave

    def codifica(self,
            testoInChiaro
        ) -> str:
        
        alfabeto: list[str] = list(string.ascii_lowercase)
        cifratura: str = ''
        nuova_chiave = self.chiave % len(alfabeto)
        for item in testoInChiaro:
            if item in alfabeto:    
                nuovo_indice =  (alfabeto.index(item)+nuova_chiave)\
                                 %len(alfabeto)
                cifratura += alfabeto[nuovo_indice]
            else:
                cifratura += item
        return cifratura
    
    def decodifica(self,
            testoCifrato
        ) -> str:
        alfabeto: list[str] = list(string.ascii_lowercase)
        cifratura: str = ''
        nuova_chiave = self.chiave % len(alfabeto)
        for item in testoCifrato:
            if item in alfabeto:    
                nuovo_indice =  (alfabeto.index(item)-nuova_chiave)\
                                 %len(alfabeto)
                cifratura += alfabeto[nuovo_indice]
            else:
                cifratura += item
        return cifratura   

    def leggi_file(self,
            path: str
    ) -> str:
        with open(path, 'r') as file:
            return file.read()
        
    def scrivi_file(self,
            contenuto: str,
            nome_file: str,
    ) -> None:
        with open(nome_file, 'w') as file:
            file.write(contenuto)       


class CifratoreACombinazione(
    CodificatoreMessaggio,
    DecodificatoreMessaggio
):
    n_cifrature: int = 0

    def __init__(self,
            n_cifrature
    ) -> Self:
        self.cifrature = n_cifrature

    def codifica_singola(self,
            testo
    ) -> str:
        if len(testo) % 2 == 0:
            meta: int = len(testo) // 2
        else:
            meta: int = len(testo) // 2 + 1

        prima_meta: str = testo[:meta]
        seconda_meta: str = testo[meta:]
        
        ip: int = 0
        isec: int = 0
        codificato: str = ''
        
        for i in range(len(testo)):
            if (ip + isec) % 2 == 0:
                if ip < len(prima_meta):
                    codificato += prima_meta[ip]
                    ip += 1
            else:
                if isec < len(seconda_meta):
                    codificato += seconda_meta[isec]
                    isec += 1
        return codificato      

    def codifica(self, 
            testo
    ) -> str:
        codificato = testo
        for i in range(self.cifrature):
            codificato = self.codifica_singola(codificato)
        return codificato
    
    def decodifica_singola(self,
                testo
    ) -> str:
        prima_meta: str = ''
        seconda_meta: str = ''
        i: int = 0
        for item in testo:
            if i % 2 == 0:
                prima_meta += item
            else:
                seconda_meta += item
            i += 1
        completo: str = prima_meta + seconda_meta
        return completo
    
    def decodifica(self,
            testo: str
    ) -> str:
        decodificato: str = testo
        for i in range(self.cifrature):
            decodificato = self.decodifica_singola(decodificato)
        return decodificato

        



# Test CifratoreAScorrimento
c1 = CifratoreAScorrimento(3)
chiaro = "ciao mondo"
cifrato = c1.codifica(chiaro)
decifrato = c1.decodifica(cifrato)

print("Originale:", chiaro)
print("Cifrato:", cifrato)
print("Decifrato:", decifrato)

# Test CiffratoreACombinazione
c2 = CifratoreACombinazione(3)
chiaro2 = "messaggio"
cifrato2 = c2.codifica(chiaro2)
decifrato2 = c2.decodifica(cifrato2)

print("\nOriginale:", chiaro2)
print("Cifrato:", cifrato2)
print("Decifrato:", decifrato2)
