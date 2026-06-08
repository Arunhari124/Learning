import json
import time
import password_encryption

class sign_page():
    #class to handle all login process
    def sign_in():
        #function to check already registered user id and pass
        
        user_id=input("Mail or Phone_number or Name : ")
        user_pass_org=input("ENTER THE PASSWORD: ")
        user_pass=password_encryption.password_encrypter(user_pass_org)
        
        
          
        for key, values in data.items():
            if user_id in values:
                if user_pass in data:
                    time.sleep(1)
                    print("please wait....")  
                    time.sleep(2)
                    print("Login successful")
                else:
                    print("incorrect password/user id ")
            
            
    def sign_up():
        #function to create a new user account
        user_name_id=input("|__________________Name:")
        user_phone_id=input("|_____Phone NUmber-+91:")
        for  user_data in data.items():

            if user_phone_id in user_data:
                print("phone number already exists")
                return
        user_email_id=input("|_________________Email:")
        for  user_data in data.items():

            if user_email_id in user_data:
                print("!Email aldready exist")
                return
        user_pass_org=input("|_______________Password:")
        user_pass=password_encryption.password_encrypter(user_pass_org)
        forget_password_hint=input("Enter a HINT :")
        #checks hint and password  is equal or not
        if forget_password_hint==user_pass_org:
            print("Your 'HINT' and 'Password; cannot be same:!")
            forget_password_hint=input("Enter a HINT :")
       
        user_hint=forget_password_hint
        user_data=[user_email_id,user_name_id,user_phone_id]
        
        forget[user_pass]=user_hint
        data[user_pass]=user_data
        
        with open("forget.json", "w") as file:
            json.dump(forget, file, indent=4)
        with open("sample.json", "w") as file:
            json.dump(data, file, indent=4)
            
    def reset_pass():
        #function to show pass using hint 
        user_id=input("Mail or Phone_number or Name : ")
        for key ,values in data.items():
            if (user_id in values):
                user_hint=input("Enter the hint of your password: ")
                for key1,values2 in forget.items():
                    if user_hint == values2:
                        
                        user_pass_new=input("enter new password:")
                        user_new_hint=input("enter _new hint:")
                        user_pass=password_encryption.password_encrypter(user_pass_new)
                    
                    else: 
                        print("invalid")
                
            else: 
                print("invalid")
            
            
        forget[user_pass] = user_new_hint
        forget.pop(key1)
        data[user_pass]=data.pop(key)
        with open("forget.json", "w") as file:
                    json.dump(forget, file, indent=4)
        with open("sample.json", "w") as file:
                    json.dump(data, file, indent=4)            
            
                   
                
        
            
    
try:
        #json file reading sample.json
        with open("sample.json", "r") as file:
            data = json.load(file)
        #json file reading forget.json
        with open("forget.json","r") as file:
            
            forget=json.load(file)
except Exception:
        data = {}
        forget={}