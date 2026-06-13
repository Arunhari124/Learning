import json

def deposit(id):
        
        balance=user_info[id][4]
        money=float(input("Enter the money to deposit(in digits) :"))
        balance +=money
def balance(id):
        balance=user_info[id][4]
        print(balance)
def withdraw(id):
        balance=user_info[id][4]
        money=float(input("Enter the money to withdraw(in digits) :"))
        balance -=money
        
        
        
try:
        
        with open("user_account.json", "r") as file:
            user_info = json.load(file)           
except Exception:
        
       user_info={}