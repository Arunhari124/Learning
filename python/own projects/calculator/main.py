from All_basic_calculations import calc
from home_page import home
import time



if __name__=="__main__":

    home()
    time.sleep(1.5)
    calc_method=input("Enter which type of calcualtion needs :")

    calc.calcu()