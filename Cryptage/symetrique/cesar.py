user_input_text = str(input("Saisir le mot pour chiffre:"))
user_input_key = input("Saisir le Key:")[0]
C=list()
for i in user_input_text:
    if i.isupper():
            c=chr((((ord(i)-ord('A'))-(ord(user_input_key)-ord('A')))%26)+ord('A'))
            C.append(c)

    elif i.islower():

        c=chr((((ord(i)-ord('a'))-(ord(user_input_key)-ord('A')))%26)+ord('a'))
        C.append(c)

    else:
        C.append("")

print(C)
message_chiff="".join(C)
print(message_chiff)

