from classses import calc
import time

def main():
    num1=float(input("ENter number = "))
    time.sleep(0.5)
    oper=input("+ - x / ")
    time.sleep(0.5)
    num2=float(input("Enter number "))
    y=calc(num1,num2)
    if oper=="+":
            
        time.sleep(0.5)
        return y.add()
        print()
            
    elif oper=="-":
            
        return y.sub()
        print()
            
    elif oper=="x":
            
        return y.multi()
        print()
            
    elif oper=="/":
            
        return y.div()
        print()
            
    else:
            
        print("-----------------syntax  error---------------------")




