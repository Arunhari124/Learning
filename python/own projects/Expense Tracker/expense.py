

def expense():
    amount=float(input("ENter your monthly income: "))
    expene={}
    is_running=True 
    while is_running:
    
        exp=input("Enter the item:/S:")
    
        if exp.upper()=="S":
            is_running=False
        else:
            amnt=float(input("ENTE THE Amont:"))
            expene[exp]=amnt


    print(expene)  
    s=sum(expene.values())
    if s>amount:
        print("losss")
    elif s == amount:
        print("tie")
    else:
        print("WON")
    print(s)
    
    
expense()