from typing import Self
from Pagamento import Pagamento

class PagamentoContanti(Pagamento):

    __importo: float

    #def __init__(self):


    def inPezziDa(self) -> str:
        importo: float = round(self.getPagamento(), 2)
        tagli: list[float] = [
            500, 200, 100, 
            50, 20, 10, 5,
            2, 1, 0.50, 0.20,
            0.10, 0.5, 0.2, 0.1
        ]
        pezzi_da: dict = {}
        print(f'Per pagare sono necessarie:')
        for n in tagli:
            while importo >= n:
                    importo -= n
                    if n not in pezzi_da:
                        pezzi_da[n] = 1
                    else:
                        pezzi_da[n] += 1
                    continue
                
        for ban, n in pezzi_da.items():
            match (ban, n):
                case (ban, 1) if ban > 4:
                    print(f'{n} banconota da {ban}')
                case (ban, n) if ban > 4:
                    print(f'{n} banconote da {ban}')
                case (ban, 1) if ban < 4:
                    print(f'{n} moneta da {ban}')
                case (ban, n):
                    print(f'{n} monete da {ban}')

p1 = PagamentoContanti()
p1.setPagamento(437893.45)
p1.inPezziDa()
