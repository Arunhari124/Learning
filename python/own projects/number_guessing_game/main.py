from random_numgen import rand
from random_numgen import defualt_rand

y=input("D for defualt values \n F to edit random values range:")
if y.upper()=="F":
    num1=int(input("start no:"))
    num2=int(input("end no:"))
    rand(num1,num2)
    
elif y.upper()=="D":
    defualt_rand()


