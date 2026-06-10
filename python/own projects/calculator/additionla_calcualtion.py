class additional():
    def factorial(n):
        
        if n == 0 or n == 1:
            return 1
   
        else:
            return n * additional.factorial(n-1)
    
    
    

