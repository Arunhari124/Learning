from classses import chad_functions
import time
import difflib

def get_similarity(a, b):
    return difflib.SequenceMatcher(None, a, b).ratio()


    
    
def main(user_input,user_name):
    obj=chad_functions(user_name)
    z=obj.basic_response()
    
    score = get_similarity(user_input, "hello") 
    for key, values in z.items():
            if isinstance(key, tuple):
                
                if score > 0.1:
                        
                    time.sleep(0.5)
                    print(values)
                    print()
        
                        
                      
