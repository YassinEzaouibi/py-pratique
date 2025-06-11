import random

### Key generation ###

p= 1434691649
g= 3
# x= random.randint(2,p-2) Kpr
x= 365502819
beta = pow(g,x,p)

# Kpr (x)
print(f"Clé privée (x): ({x})")
# Kpb (p, g, beta)
print(f"Clé publique (p, g, beta): ({p}, {g}, {beta})")

### Encryption ###

m= 20033002
print(f"Message: {m}")

# k= random.randint(2,p-2)
k= 1200063362
c1 = pow(g,k,p)
c2 = (m * pow(beta,k,p)) % p
print(f"Ciphertext: ({c1}, {c2})")

### Decryption ###
c1_inv = pow(c1,-x,p)
m_dek = c1_inv*c2 % p
print(f"Message decrepte: {m_dek}")
