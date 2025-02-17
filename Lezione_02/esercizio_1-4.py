n = int(input("Inserire numero di 4 cifre:"))
m = n // 1000
c = n // 100 - m * 10
d = n // 10 - m * 100 - c * 10
u = n - m * 1000 - c * 100 - d * 10
print (m)
print (c)
print (d)
print (u)