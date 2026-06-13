def initial_deposit():
    print("your current balance is 0$")
    y_n=input("would you like to deposit some money?[Y]yes,[N]no:")
    balance=0
    if y_n.upper()=="Y":
        
        try:
            money=float(input("Enter the amount(in digits):"))
        except Exception:
            money=float(input("Enter the amount(in digits):"))
            
        balance=balance+money
        return balance
    else:
        return balance