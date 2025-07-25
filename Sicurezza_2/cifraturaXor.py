testo: str = '''Scrivere un programma PYTHON che a partire da una stringa 
la cifra con la tecnica XOR Successivamente mostrare che la stringa 
cifrata, riapplicando lo stesso XOR, torna la stringa originale
Per fare lo XOR utilizzate un solo valore: 57 Quindi data la stringa 
di esempio “Nel mezzo del cammin di nostra vita”, dovete fare per ogni 
carattere della stringa lo xor con il valore 57 “N” xor 57, “e” xor 57,
… Ottenendo una lista di numeri es: 78 (che è il codice asciii  della 
lettera N) xor (si indica con il simbolo ^) => 78 ^ 57 = 119 E così via 
per tutta la stringa. Al termine stampare la lista di numeri ottenuti
In fondo a partire dalla lista di numeri, riapplicare lo xor sempre con 
57 e quindi ottenere (ricostruendola) la stringa originale NB: potreste 
utilizzare input(“…”) in modo da leggere sia la stringa da cifrare, sia 
il valore segreto da applicare come xor'''

chiave: int = 57
def cifratura(da_cifrare, chiave: int):
    cifrato: list[int] = []
    for char in da_cifrare:
        cifratura: int = ord(char)^chiave
        cifrato.append(cifratura)
    return cifrato

def decifratura(da_decifrare: list[int], chiave: int):
    decifrato: str = ''
    for element in da_decifrare:
        cod_char: int = element^chiave
        decifrato += chr(cod_char)
    return decifrato

cifratura_: list[int] = cifratura(input('inserisci messaggio da cifrare: '), 
                                  int(input('inserisci chiave di cifratura: ')))
print(cifratura_)
decifratura_ : str = decifratura(cifratura_, 
                                 int(input('inserisci chiave di decifratura: ')))
print(decifratura_)
