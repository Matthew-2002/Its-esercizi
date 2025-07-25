from abc import ABC, abstractmethod
from typing import Self

class Volo(ABC):

    codice_volo: str
    capacita_max: int

    def __init__(
            self, codice_volo: str, 
            capacita_max: int, 
            ) -> Self:
    
        self.codice_volo = codice_volo
        self.capacita_max = capacita_max
        self.prenotazioni = 0

    @abstractmethod
    def prenota_posto():
        pass

    @abstractmethod
    def posti_disponibili():
        pass


class VoloCommerciale(Volo):

    capacita_max: int
    codice_volo: str
    
    posti_economica: int
    posti_buisness: int
    posti_prima: int

    prenotazioni_economica: int
    prenotazioni_business: int
    prenotazioni_prima: int

    def __init__(
            self, 
            codice_volo: str, 
            capacita_max: int
                 ) -> Self: 
        super().__init__(
            codice_volo, 
            capacita_max
            )
        
        self.posti_economica = int((capacita_max/100)*70)
        self.posti_buisness = int((capacita_max/100)*20)
        self.posti_prima = int((capacita_max/100)*10)

        self.prenotazioni_economica = 0
        self.prenotazioni_business = 0
        self.prenotazioni_prima = 0

    def posti_disponibili(self) -> dict[str, int]:

        elenco_posti: dict[str, int] = {
            'posti disponibili': (self.posti_prima +
                                  self.posti_buisness +
                                  self.posti_economica),
            'posti prima': self.posti_prima,
            'posti buisness': self.posti_buisness,
            'posti economica': self.posti_economica
        }
        return elenco_posti
    
    def prenota_posto(self, 
            n_posti: int, 
            classe: str
            ) -> None:
                
        if n_posti <= 0:
            return f'non puoi prenotare {n_posti} posti'
        
        if n_posti > self.posti_disponibili()['posti disponibili']:
            return 'Non ci sono abbastanza posti sul volo selezionato'
        
        chiave: str = 'posti ' + classe  

        if n_posti > self.posti_disponibili()[chiave]:
            return f'Non ci sono abbastanza posti disponibili \
nella classe {classe}'
        
        match classe:
            case 'buisness':
                self.posti_buisness -= n_posti
                self.prenotazioni_business += n_posti                        
            case 'prima':
                self.posti_prima -= n_posti
                self.prenotazioni_prima += n_posti
            case 'economica':
                self.posti_economica -= n_posti
                self.prenotazioni_economica += n_posti
        self.prenotazioni += n_posti

class VoloCharter(Volo):

    capacita_max: int
    codice_volo: str

    prezzo: float
    
    def __init__(self, 
            codice_volo: str, 
            capacita_max: int, 
            prezzo: float
            ) -> Self:

        super().__init__(
            codice_volo,
            capacita_max
            )
        
        self.prezzo = prezzo

    def prenota_posto(self) -> str:

        if self.prenotazioni == 0:
            self.prenotazioni = self.capacita_max
            return f'acquisto andato a buon fine. \
Totale spesa ${self.prezzo*self.capacita_max}'
        
        return f'Acquisto non completato per mancanza di posti'
    
    def posti_disponibili(self) -> int:

        return self.capacita_max - self.prenotazioni
    
class CompagniaAerea:

    nome: str
    prezzo: float
    flotta: list[VoloCommerciale]

    def __init__(self, 
            nome, 
            prezzo
            ) -> Self:
        
        self.nome = nome
        self.prezzo = prezzo
        self.flotta = []

    def aggiungi_volo(self, 
                volo_commerciale: VoloCommerciale
                ) -> None:
        
        if type(volo_commerciale) == VoloCommerciale:
            self.flotta.append(volo_commerciale)
    
    def rimuovi_volo(self,
                volo_commerciale: VoloCommerciale
                ) -> None:
        
        if type(volo_commerciale) == VoloCommerciale:
            self.flotta.remove(volo_commerciale)

    def mostra_flotta(self) -> None:

        print('Flotta:')
        for item in self.flotta:
            print(f'    codice Volo: {item.codice_volo}')
        
    def guadagno(self) -> float:

        guadagno: float = 0
        for item in self.flotta:
            guadagno += item.prenotazioni_prima*self.prezzo*3
            guadagno += item.prenotazioni_business*self.prezzo*2
            guadagno += item.prenotazioni_economica*self.prezzo
        guadagno = round(guadagno, 2)
        return guadagno
    
if __name__ == '__main__':
   
    volo1 = VoloCommerciale('CA5789', 100)
    print(volo1.posti_disponibili())

        


            

            
    
        



        



        

