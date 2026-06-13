from random_numgen import rand
import time
from random_numgen import defualt_rand

y=input("D for defualt values  F to edit random values range:")
if y.upper()=="F":
    num1=int(input("start no:"))
    num2=int(input("end no:"))
    
    is_running=True
    while is_running:
        x=rand(num1,num2)
        user_num=int(input(f"ENter a number btw {num1} and {num2} "))
        
        if x==user_num:
            print("\n\nWON!")
            time.sleep(2)
        elif user_num > num2:
            print(f"MUST BE LESS THAN {num2}")
        
        else:
            print(f"YOURS:{user_num}|BOT:{x}")
        
elif y.upper()=="D":
    
    is_running=True
    while is_running:
        x=defualt_rand()
        user_num=int(input("ENter a number btw 1 and 10 "))
        
        if x==user_num:
            print("\n\nWON!")
            time.sleep(2)
        elif user_num > 10:
            print("MUST BE LESS THAN 10")
        
        else:
            print(f"YOURS:{user_num}|BOT:{x}")
            


