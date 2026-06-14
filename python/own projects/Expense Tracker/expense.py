
import json
def expense():
    amount=float(input("ENter your monthly income: "))
    
    is_running=True 
    while is_running:
    
        exp=input("Enter the item:/S:")
          
    
        if exp.upper()=="S":
            is_running=False
        else:
            amnt=float(input("ENTE THE Amont:"))
            expene[exp]=amnt
            with open("expense.json", "w") as file:
                    json.dump(expene, file, indent=4)

    print(expene)  
    s=sum(expene.values())
    if s>amount:
        print("losss")
    elif s == amount:
        print("tie")
    else:
        print("WON")
    print(s)
    


try:
    with open("expense.json", "r") as file:
            expene = json.load(file)   
except Exception:
    expene={}
    
        
expense()