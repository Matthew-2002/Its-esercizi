'''Safe Square Root: Write a function safe_sqrt(number) 
that calculates the square root of a number using math.sqrt(). 
Handle ValueError if the input is negative by returning an 
informative message.'''


import math

def safe_sqrt(n):
    if n < 0:
        raise Exception(f"Il numero di cui vuoi calcolare la\
 radice non può essere negativo: {n}")
    else:
        return round(math.sqrt(n), 2)
    
print(safe_sqrt(int(input("Inserisci numero di cui vuoi sapere la radice quadrata: "))))
