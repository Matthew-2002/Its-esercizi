somma:int = 0
for i in range(1,11):
    somma += i
print(somma)

somma:int = 0
for i in range(20,38):
    somma += i
print(somma)

somma:int = 0
for i in range(35,50):
    somma += i
print(somma)

def sommarange(a:int, b:int):
    somma = 0
    for i in range(a,b+1):
        somma += i
    return somma

print(sommarange(1, 10))

print(sommarange(20, 37))

print(sommarange(35, 49))