n=3512

#with open("numero1.dat", "wb") as f:
#    f.write(n.to_bytes(4, byteorder="little"))
#
#with open("numero2.dat", "wb") as f:
#    f.write(n.to_bytes(4, byteorder="big"))
#
#s = 'Ciao'
#with open("numero3.dat", "w") as f:
#    f.write(s)

def S2N(s):
    tot = 0
    exp = 0
    for c in s:
        tot += 256 ** exp * ord(c)
        exp += 1
    return tot

def S2Ne(s):
    tot = 0
    for c in s:
        tot = (tot << 8) | ord(c)
    return tot

print(S2Ne('Ciao'))
print(S2N('Ciao'))