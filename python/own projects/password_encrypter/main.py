from encrypting import password_encrypter




if __name__=="__main__":
    password=input("Enter password to encrypt:")
    encrypted=password_encrypter(password)
    print(f"Encrypted password of your password is\n                               copy👇\n                       ====   |{encrypted}|       =====\n\n")