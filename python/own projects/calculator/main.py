from All_basic_calculations import calc
from home_page import home
import time
from additionla_calcualtion import additional



if __name__=="__main__":

    home()
    time.sleep(1.5)
    calc_method=input("Enter which type of calcualtion needs :")
    if calc_method=="1":
        n=int(input("Number for factorial"))
        print(additional.factorial(n))
    elif calc_method=="2":
        n=float(input("Enter the number:"))
        p=float(input("Enter the power:"))
        print(additional.exponent(n,p))
    else:

        calc.calcu()