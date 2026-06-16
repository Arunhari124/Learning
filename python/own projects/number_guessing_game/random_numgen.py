
import numpy as np
def rand(num1,num2):
    rng=np.random.default_rng()
    print(f"values will be btw{num1} and {num2}")
    return rng.integers(num1,num2)

    

def defualt_rand():
    rng=np.random.default_rng()

    print("values will be btw 1 and 10")
    return rng.integers(1,11)

    
    
    
