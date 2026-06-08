from classses import chad_functions
import time
import random as rn
import difflib

def get_similarity(a, b):
    return difflib.SequenceMatcher(None, a, b).ratio()

def motive(user_input,user_name):
    obj=chad_functions(user_name)
    m=obj.motivate()    
    score = get_similarity(user_input, "motivation")  
    if score > 0.2:
        key,value =rn.choice(list(m.items()))
            
        time.sleep(0.5)
        
        print( f"{value}")
        print()
        
            
            
            
            
            
            
            
            

            

             
            
            
            
