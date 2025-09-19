class Frazione:

    def __init__(self, num, den):
        
        self.numSetter(num)
        self.denSetter(den)
    
    
    def value(self) -> float:

        return round(self.num/self.den, 3)

    def __str__(self) -> str:

        return f'{self.num} / {self.den}'
    
    def numSetter(self, num) -> None:

        if float(num).is_integer() == False:
            self.num = 13
        else:
            self.num = num
    
    def denSetter(self, den) -> None:

        if float(den).is_integer() == False or den == 0:
            self.den = 5
        else:
            self.den = den

def maxComDiv(n1, n2) -> int:

    mcd: int = 0

    if n1 > n2:

        n1 , n2 = n2, n1

    for i in range(1, (n2//2)+1):

        if n2 % i == 0 and n1 % i == 0:
            
            mcd = i
    
    return mcd

def semplifica(listaFraz: list[Frazione]) -> list[Frazione]:

    semplificati: list[Frazione] = []
    
    for item in listaFraz:

        mcd = maxComDiv(item.num, item.den)
        
        if mcd != 1:
        
            nuovoDen: int = item.den / mcd
            nuovoNum: int = item.num / mcd
            nuovaFraz: Frazione = Frazione(nuovoNum, nuovoDen)
            semplificati.append(nuovaFraz)
        
        else:

            semplificati.append(item)

    return semplificati

def fractionCompare(listaFraz: list[Frazione], l2) -> None:
    
    for i in range(len(l2)):

        print(f"Valore originale: {listaFraz[i].value()}\
 --- valore frazione ridotta: {l2[i].value()}")
        
if __name__ == "__main__":

    l: list[Frazione] = [
        Frazione(2.5, 0),
        Frazione(1, 2),
        Frazione(2, 4),
        Frazione(3, 5),
        Frazione(6, 9),
        Frazione(4, 7),
        Frazione(24, 36),
        Frazione(12, 36),
        Frazione(40, 60),
        Frazione(5, 11),
        Frazione(10, 45),
        Frazione(42, 78),
        Frazione(9, 15)
        ]
    l_s: list[Frazione] = semplifica(l)
    fractionCompare(l, l_s)








    


        
