import random
import string




def password_encrypter(user_pass):
    encrypted_text=""
    for passs in user_pass:
        index=chars.index(passs)
        encrypted_text += key[index]
    return encrypted_text



chars=" " + string.punctuation + string.digits + string.ascii_letters
chars=list(chars)
key=chars.copy()
random.seed(42)
random.shuffle(key)


