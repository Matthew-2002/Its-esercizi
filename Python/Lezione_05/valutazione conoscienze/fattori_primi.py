def prime_factors(n: int) -> list[int]:
    fattori = []
    n_ = n
    div = 2
    while div * div <= n_:
        if n % div == 0:
            fattori.append(div)
            n //= div
        else:
            div += 1 if div == 2 else 2
    return fattori

def print_factors(fattori: list[int]) -> list[str]:

    formatted_factors: list[str] = []
    for i in range(len(fattori)):
        if i == 0:
            count = 1
        else:
            if fattori[i-1] != fattori[i]:
                count = 1
            else:
                count += 1
        if i == (len(fattori) - 1):
            formatted_factors.append(str(f'{fattori[i]}**{count}') \
                if count != 1 else str(fattori[i]))
        else:
            if fattori[i] != fattori[i+1]:
                formatted_factors.append(str(f'{fattori[i]}**{count}') \
                    if count != 1 else str(fattori[i]))
    return formatted_factors

print(print_factors(prime_factors(12345678901)))
    
