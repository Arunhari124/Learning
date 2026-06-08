#Login & Signup System

from userlogin import sign_page
if __name__=="__main__":
    print("|---------------------WELCOME---------------------|")
    print("\n \n")
    sign=input("|---------------------Register[R]---------------------|\n|---------------------Login[L]------------------------|\n|---------------------Forget password(F)--------------|\n-----------------------------------------------------:")
    s=0
    
    if sign.upper() == "L":
        sign_page.sign_in()

    elif sign.upper() == "R":
        sign_page.sign_up()

    elif sign.upper() == "F":
        sign_page.reset_pass()
        
        
    elif sign =="":
        sign_page.sign_in()

    else:
        print("Invalid option")
    
 

