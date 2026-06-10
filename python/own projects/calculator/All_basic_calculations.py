#all basic calculation Addition,Subtraction,Multiplication,division 




class Calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    
    def add(self):
        return self.num1+self.num2
    def sub(self):
        return self.num1-self.num2
    def multi(self):
        return self.num1*self.num2
    def divi(self):
        return self.num1/self.num2
    
    
class calc(Calculator):
    def calcu():
        while True:
            num1 = float(input("Number="))
            oper=input("_____+_____\n_____-_____\n_____x_____\n_____/____\n__=")
            num2 = float(input("Number="))
    
            if oper=="+":
                calculator = Calculator(num1, num2)
                total = calculator.add()
            elif oper=="-":
                calculator = Calculator(num1, num2)
                total = calculator.sub()
            elif oper=="x":
                calculator = Calculator(num1, num2)
                total = calculator.multi()
            else:
                calculator = Calculator(num1, num2)
                total = calculator.divi()

            print(total)

            while True:
             
                oper=input("_____+_____\n_____-_____\n_____x_____\n_____/_____\n__=")
                num1 = float(input("Number="))
                #num2 = int(input("Number="))
        
                if oper=="+":
                    calculator = Calculator(num1, total)
                    total =  calculator.add()
                    print(total)
                elif oper=="-":
                    calculator = Calculator(num1, total)
                    total = calculator.sub()
                    print(total)
                elif oper=="x":
                    calculator = Calculator(num1, total)
                    total =  calculator.multi()
                    print(total)
                else:
                    calculator = Calculator(num1, total)
                    total = calculator.divi()
                    print(total)  
    

        
        

        