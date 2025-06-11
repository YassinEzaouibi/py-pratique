from collections import Counter

def analyser_frequence(texte):
    return Counter(texte)

def trouver_cle_vigenere(texte_chiffre, longueur_cle):
    # Diviser le texte chiffré en blocs de la longueur de la clé
    blocs = [texte_chiffre[i::longueur_cle] for i in range(longueur_cle)]
    cle = []

    # Pour chaque bloc, effectuer une analyse de fréquence
    for bloc in blocs:
        frequence = analyser_frequence(bloc)
        lettre_plus_frequente = max(frequence, key=frequence.get)
        cle.append(chr((ord(lettre_plus_frequente) - ord('E')) % 26 + ord('A')))

    return ''.join(cle)

# Exemple de texte chiffré
texte_chiffre = "WAKKQLERSCGBA"
longueur_cle = 5  # Remplacez par la longueur de la clé que vous avez devinée
cle = trouver_cle_vigenere(texte_chiffre, longueur_cle)

print("Clé supposée:", cle)
