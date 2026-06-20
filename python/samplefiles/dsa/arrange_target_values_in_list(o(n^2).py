#  0 1 2 3 4  5  6 7 8 9 10
f=[6,1,6,8,10,4,15,6,3,5,6]
t=6

for i in range(len(f)):
    if f[i]==t:
        for j in range(len(f)-1,i,-1):
            if f[j]==t:
                continue
            else:
                temp=f[i]
                f[i]=f[j]
                f[j]=temp
                break
                
                
            
print(f)