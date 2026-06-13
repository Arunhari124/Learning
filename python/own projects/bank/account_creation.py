
import json
from password_encrypter import password_encrypter
from id_generator import id_gen
from deposit import deposit
def account_creating():
    import json
    import time
    
    name=input("Enter your name:")
    mobile_number=input("Enter the mobile number: ")
    address=input("Enter your address: ")
    time.sleep(1)
    password=input("Enter your password ")
    password1=input("Enter your password ")
    
    if password==password1:
        time.sleep(1)
        id=str(id_gen())
        is_running=True
        while is_running:
            if id in user_info:
                id=str(id_gen())
                is_running=False
            else:
                is_running=False
            
            encrypted_password=password_encrypter(password)
            balance=deposit()
            l1=[name,mobile_number,address,encrypted_password,balance]
            user_info[id]=l1
            
            print(f"YOUR USER_ID={id}")
            with open("user_account.json", "w") as file:
                    json.dump(user_info, file, indent=4)
        
try:
        
        with open("user_account.json", "r") as file:
            user_info = json.load(file)           
except Exception:
        user_info={}
        

#account_creating()
        
