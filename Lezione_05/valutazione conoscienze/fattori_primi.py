import math

def prime_factors(n: int) -> list[int]:
    fattori: list[int] = []
    div: int = 2
    while n > 1:
        if n % div == 0:
            n /= div
            fattori.append(div)
        else:
            div += 1
    return fattori

print(prime_factors(99999999999999999999))
    
