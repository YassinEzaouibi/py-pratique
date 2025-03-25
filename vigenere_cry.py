user_input_text = str(input("Saisir le mot pour chiffre:"))
user_input_key = input("Saisir le Key:")
# user_input_text = "LICENCEMAIM"
# user_input_key = "FPDN"
l=len(user_input_key)
C=list()
for i in range(len(user_input_text)):
        c=chr((((ord(user_input_text[i])-ord('A'))+(ord(user_input_key[i%l])-ord('A')))%26)+ord('A'))
        C.append(c)

print(C)
message_chiff="".join(C)
print(f'le mot: ' + user_input_text)
print(f'Key: ' + user_input_key)
print(f'le mot chiffre: ' + message_chiff)

