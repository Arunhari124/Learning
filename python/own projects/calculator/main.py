from All_basic_calculations import calc
from home_page import home
import time
from additionla_calcualtion import additional



if __name__=="__main__":

    home()
    time.sleep(1.5)
    while True:
        calc_method=input("Enter which type of calcualtion needs \n 1 for factorial \n 2 for exponentail calc \n 3 for square root \n 4 for cube root \n type[x]for normal calculatoion:")
        if calc_method=="1":
            n=int(input("Number for factorial "))
            print(additional.factorial(n))
        elif calc_method=="2":
            n=float(input("Enter the number:"))
            p=float(input("Enter the power:"))
            print(additional.exponent(n,p))
        elif calc_method=="3" :
            n=float(input("Enter the number:"))
            print(additional.squart(n))
        elif calc_method =="4":
            n=float(input("Enter the number:"))
            print(additional.cubert(n))
        else:
            calc.calcu()