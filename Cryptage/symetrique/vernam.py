def letter_to_num(c):
   return ord(c) - ord('A')


def num_to_letter(n):
   return chr(n + ord('A'))


def vernam_encrypt(plaintext, key):
   ciphertext = ''
   for p, k in zip(plaintext, key):
      p_num = letter_to_num(p)
      k_num = letter_to_num(k)
      c_num = (p_num + k_num) % 26
      ciphertext += num_to_letter(c_num)
   return ciphertext


def vernam_decrypt(ciphertext, key):
   plaintext = ''
   for c, k in zip(ciphertext, key):
      c_num = letter_to_num(c)
      k_num = letter_to_num(k)
      p_num = (c_num - k_num) % 26
      plaintext += num_to_letter(p_num)
   return plaintext

M = "YASSIN"
K = "YASSON"


# Chiffrement
cipher = vernam_encrypt(M, K)
print("Chiffre :", cipher)

# Déchiffrement
decrypted = vernam_decrypt(cipher, K)
print("Déchiffré :", decrypted)
