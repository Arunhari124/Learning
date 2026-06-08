import math as m 
class Calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        
        return self.num1 + self.num2
    def multi(self):
        
        return self.num1 * self.num2
    def sub(self):
        
        return self.num1 - self.num2
    def div(self):
        
        return self.num1 / self.num2



class Quadratic:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def quad(self):
        x= (- self.b + m.sqrt(( self.b **2) - 4 * self.a * self.c)) / (2 * self.a)
        y= (- self.b - m.sqrt(( self.b **2) - 4 * self.a * self.c)) / (2 * self.a)
        return x , y

which_is_running=input("basic _calcultor(C) or quadratic calculator(Q)= ")
if which_is_running.lower() == "c":
    num1=float(input("Enter 1st number = "))
    oper=input("Enter \n+ \n- \nx \n/ \n =  ")
    num2=float(input("ENter 2nd number = "))

    calculation=Calculator(num1,num2)
    if oper == "+":
        print(calculation.add())
    elif oper == "-":
        print(calculation.sub())
    elif oper == "x":
        print(calculation.multi())
    elif oper == "/":
        print(calculation.div())
    else:
        print("error")
elif which_is_running.lower() == "q":
    a=int(input("a= "))
    b=int(input("b= "))
    c=int(input("c= "))
    quadratic=Quadratic(a,b,c)

    print(quadratic.quad())