import random

# p et q 16 bits
p= 17597
q= 21187
n= p*q
phi_n= (p-1)*(q-1)
# e & phi_n -> pgcd(e,phi_n)=1
# e= random.randint(2,phi_n)
# e= random((p-1)*(q-1))
e= 295078919
d= pow(e,-1,phi_n)
m= 19731978

c= pow(m,e,n)
m_dechiffre= pow(c,d,n)

# Kpb (n, e)
print(f"Clé publique (n, e): ({n}, {e})")
# Kpr (n, d)
print(f"Clé privée (n, d): ({n}, {d})")
print(f"Message original: {m}")
print(f"Message chiffré: {c}")
print(f"Message déchiffré: {m_dechiffre}")