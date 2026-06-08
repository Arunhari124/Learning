
#hi this is a chat bot (basic version)
from classses import chad_functions 
from classses import calc
import allcalculation
import jokes
import motivation
import weather
import basicresponses
import random as rn
import time

is_running=True

print("-------Hi welcome to chad,GPT------- ")

user_name=input("what is your name : ")

print()

time.sleep(0.5)
 

while is_running:
    
    user_input=input("What you need to know:\n m for motivation \n j for jokes \n w for weather \n c for calculator \n o to exit =")
    
    x=any(char.isdigit() for char in user_input)
    
    #calculator part
    if x == True or user_input.lower() in ("calculator","calculation","c"):
        
        result=allcalculation.main()
        
        print(result)
        
        print()
        
      
    elif x == False:
       
        #joke call  
        jokes.jok(user_input,user_name)
        
        #motivation call
        motivation.motive(user_input,user_name)
        
        #weather call
        weather.weath(user_input,user_name)
        
        #basic response
        basicresponses.main(user_input,user_name)
        
    elif user_input.lower()in ("stop","o"):
        
        is_running=False       

            
  