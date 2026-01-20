from Cry import number

# Genera un numero primo di 2048 bit
p = number.getPrime(2048)
generatore: int = 7

alice_priv: int = 11
bob_priv: int = 14

alice_public = pow(generatore, alice_priv, p_pubbl)
bob_public = pow(generatore, bob_priv, p_pubbl)

print(alice_public, bob_public)