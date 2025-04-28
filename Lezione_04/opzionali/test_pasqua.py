def transform(x: int) -> int:
    if x % 2 == 0:
        x /= 2
    else:
        x *= 3
        x -= 1
    return x

def calcola_stipendio(ore_lavorate: int) -> float:
    stipendio: float = 0
    if ore_lavorate <= 40:
        stipendio += ore_lavorate*10
    else:
        stipendio = 400
        ore_lavorate -= 40
        stipendio += ore_lavorate*15
    return stipendio

def print_seq(): 
    
    print("Sequenza a):")
    for i in range(1,8):
        print(i)
    print()

    print("Sequenza b):")
    for i in range(3,24,5):
        print(i)
    print()

    print("Sequenza c):")
    for i in range(20,-11,-6):
        print(i)
    print()

    print("Sequenza d):")
    for i in range(19,52,8):
        print(i)
    print()
    
    return

def integerPower(base, esponente) -> int:
    n = 1
    for i in range(esponente):
        n *= base
    return n

import math
def hypotenuse(cat1: float, cat2: float) -> float:
    hypotenuse = math.sqrt(cat1*cat1+cat2*cat2)
    return hypotenuse

def remove_elements(original_set: set[int], elements_to_remove: list[int]) -> set[int]:
    for item in elements_to_remove:
        if item in original_set:
            original_set.remove(item)
    return original_set

def countdown(x: int) -> None:
    for i in range (x,-1,-1):
        print(i)

def seconds_since_noon(h: int, m: int, s: int) -> int:
    seconds: int = 0
    seconds += (h*3600)
    seconds += (m*60)
    seconds += s
    return seconds

def time_difference(h1, m1, s1, h2, m2, s2) -> int:
    tot_s1: int = seconds_since_noon(h1, m1, s1)
    tot_s2: int = seconds_since_noon(h2, m2, s2)
    if tot_s1 > tot_s2:
        return tot_s1 - tot_s2
    else:
        return tot_s2 - tot_s1
    
def rimbalzo() -> None:
    
    tempo: int = 0
    altezza: float = 0.0
    velocita: float = 100.0
    rimbalzi: int = 0

    while tempo < 29:
        if altezza < 0:
            print(f"Tempo: {tempo} Rimbalzo!")            
            altezza *= -0.5 
            velocita *= -0.5
            rimbalzi += 1
        else:
            print(f"Tempo: {tempo} Altezza: {altezza}")
            altezza += velocita
            velocita = velocita - 96
        tempo += 1

def memorizza_file(files: list[int]) -> None:
    spazio_totale_blocchi = 1000
    blocchi_usati = 0
    for item in files:
        compresso: float = (item/5)*4
        if compresso % 512 > 256:
            blocco_file = int(compresso // 512) + 1
        else:
            blocco_file = int(compresso // 512)
        spazio_totale_blocchi -= blocco_file
        blocchi_usati += blocco_file
        if spazio_totale_blocchi < 0:
            print(f"Non è possibile memorizzare il file di {item} byte.\
 Spazio insufficiente.")
            return None
        else:
            print(f"File di {item} byte compresso in {compresso} byte e memorizzato. Blocchi usati: {blocco_file}.\
 Blocchi rimanenti: {spazio_totale_blocchi}.")