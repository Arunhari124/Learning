
def password_genarator():
    import random

    abc = "ABCDEFGHIJKLMNOPRSTUVWXYZabcdefghijklmnoprstuvwxyz1234567890-+!@#$%^&*(=[}';/.,"

    password = ""

    for _ in range(8):
        password += random.choice(abc)

    return password