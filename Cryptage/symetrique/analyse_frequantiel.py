from collections import Counter

def dechiffrer_cesar(texte, cle):
    resultat = []
    for c in texte:
        if c.isalpha():
            decalage = (ord(c.upper()) - ord('A') - cle) % 26
            resultat.append(chr(decalage + ord('A')))
        else:
            resultat.append(c)  # Garder les espaces
    return ''.join(resultat)

def analyser_frequence(texte):
    lettres = [c for c in texte.upper() if c.isalpha()]
    return Counter(lettres)

def trouver_cle(frequence, lettre_cible='E'):
    lettre_plus_frequente = max(frequence, key=frequence.get)
    return (ord(lettre_plus_frequente) - ord(lettre_cible)) % 26

# Test
# texte_chiffre = "MINSPMZC ZQ PINPWWPYNP XLESPXLETND LAAMTPO EZ XLNSTYP TYEPWWTRPYNP"
texte_chiffre = "MLNSPWZC ZQ PINPWWPYNP XLESPXLETND LAAWTPO EZ XLNSTYP TYEPWWTRPYNP"
freq = analyser_frequence(texte_chiffre)
cle = trouver_cle(freq)
print("Clé supposée:", cle)
print("Message déchiffré:", dechiffrer_cesar(texte_chiffre, cle))