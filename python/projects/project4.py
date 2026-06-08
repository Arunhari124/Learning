import random
import string


chars=" " + string.punctuation + string.digits + string.ascii_letters
chars=list(chars)
key=chars.copy()
random.shuffle(key)
#print(chars)
#print(key)

plain_text=input("Enter  a message to encrypt ")
encrypted_text=" "

for letter in plain_text:
    index=chars.index(letter)
    encrypted_text += key[index]


print(f"Original message :{plain_text}")
print(f"Encryper text :{encrypted_text}:")

encrypted_text=input("enter a message to decrypt : ")
plain_text =" "

for letter in encrypted_text:
    index=key.index(letter)
    plain_text += chars[index]



print(f"Encryper text {encrypted_text}")
print(f"original :{plain_text}")