from classses import chad_functions
import time
import difflib

def get_similarity(a, b):
    return difflib.SequenceMatcher(None, a, b).ratio()

def weath(user_input,user_name):
    obj=chad_functions(user_name)
    w=obj.weather()
    
    score = get_similarity(user_input, "w")  
    if score > 0.4:
        
            
        time.sleep(0.5)
        print(w)
        print()
        
        
        
            
            
            
            
            