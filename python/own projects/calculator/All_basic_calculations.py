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
        import time
        is_running=True

        while is_running:
            num1 = float(input("Number="))
            time.sleep(0.45)
            oper=input("_____+_____\n_____-_____\n_____x_____\n_____/____\n__  ")
            time.sleep(0.45)
            num2 = float(input("Number="))
            time.sleep(0.45)
    
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

            while is_running:
             
                oper=input("_____+_____\n_____-_____\n_____x_____\n_____/_____\n__o to stop:")
                time.sleep(0.45)
                num1 = float(input("Number="))
                time.sleep(0.45)
        
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
                elif oper=="/":
                    calculator = Calculator(num1, total)
                    total = calculator.divi()
                    print(total)
                else:
                    is_running=False
                    
                    
                      
    

        
        

        