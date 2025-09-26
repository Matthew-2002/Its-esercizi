from typing import Self

class Pagamento:

    __importo: float

    def getPagamento(self) -> float:
        return self.__importo
    
    def setPagamento(self,
        importo
    ) -> None:
        self.__importo = importo

    def dettagliPagamento(self) -> str:
        print(f"Importo del pagamento: ${self.getPagamento():.2f}")

    