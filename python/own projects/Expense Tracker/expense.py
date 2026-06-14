
import json
def expense():
    amount=float(input("ENter your monthly income: "))
    x= amount * (25/100)
    y= amount * (75/100)
    
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
        print("you spend more than you have")
    elif s == amount or s > y :
        print("try to save something next time")
    elif s == x or s < x:
        print("good joh you saved more than 25'%' of your amount")
    else:
        print("okay")
        
    


try:
    with open("expense.json", "r") as file:
            expene = json.load(file)   
except Exception:
    expene={}
    
        
expense()