def expo(base, exp):
    return pow(base,exp)

def expo_modulaire(base, exp, mod):
    return pow(base, exp, mod)

def inverse_modulaire(base, mod):
    return pow(base, -1, mod)


nombre = int(input("Saisir le nombre: "))
exponent = int(input("Saisir l'exponent: "))
modulo = int(input("Saisir le modulo: "))

print("Exponentiation: ", expo(nombre, exponent))
print("Exponentiation Modulaire: ", expo_modulaire(nombre, exponent, modulo))
print("L'inverse Modulaire: ", inverse_modulaire(nombre, modulo))