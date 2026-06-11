
import json
from password_encrypter import password_encrypter
def account_creating():
    import json
    import time
    
    name=input("Enter your name:")
    mobile_number=input("Enter the mobile number: ")
    address=input("Enter your address: ")
    time.sleep(2)
    password=input("Enter your password ")
    password1=input("Enter your password ")
    id=1
    if password==password1:
        time.sleep(1)
        encrypted_password=password_encrypter(password)
        l1=[name,mobile_number,address,encrypted_password]
        user_info[id]=l1
        with open("user_account.json", "w") as file:
                    json.dump(user_info, file, indent=4)
        
try:
        
        with open("user_accounts.json", "r") as file:
            user_info = json.load(file)           
except Exception:
        user_info={}
        

#account_creating()
        
