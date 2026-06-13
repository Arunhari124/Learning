import balance_Deposit_withdraw as bdw
def user_need(id):
    un=input("B for Balance\nD for Deposit\nW for Withdraw \n:")
    if un.upper()=="W":
        x=bdw.withdraw(id)
        return x
    elif un.upper()=="D":
        x=bdw.deposit(id)
        return x
    else: 
        x=bdw.balance(id)
        return x
        
    
