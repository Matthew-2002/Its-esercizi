def stopwhatch(func):

    def wrapper(n:int):
        import time
        start = time.time()
        func(n)
        print(time.time() - start)
    
    return wrapper

def prime_factors(n: int) -> list[int]:
    fattori = []
    n_ = n
    div = 2
    while div * div <= n_:
        if n % div == 0:
            fattori.append(div)
            n //= div
        else:
            if div == 2:
                div += 1
            else: 
                div += 2
    return fattori

timed_prime_factors = stopwhatch(prime_factors)
timed_prime_factors(38)

print(prime_factors(38))

    
