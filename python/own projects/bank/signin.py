import json
from account_creation import account_creating
from password_encrypter import password_encrypter
def sign_in():
    
        
        
        id=input("Enter your id ")
        if id in user_info:
            password=input("ENter your password ")
            encrypted_password=password_encrypter(password)
            user_info[id]
            if encrypted_password == user_info[id][3]:
                print("Login in ")
            else:
                print("ERROR")
        else:
            print("Error")

try:
        
        with open("user_account.json", "r") as file:
            user_info = json.load(file)           
except Exception:
        
       user_info={}
sign_in()