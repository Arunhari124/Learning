f = [6,1,6,8,10,4,15,6,3,5,6]
t = 6

l=0
r=len(f)-1
while l < r:
    while l < r and f[r]==t:
        r -=1
    if f[l]==t:
        f[l],f[r]=f[r],f[l]
        r-=1
    l +=1
print(f)