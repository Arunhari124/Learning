def arrr(arr):
    


    t=10
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j]==t:
                ar=[arr[i],arr[j]]
                return ar
                
arr=[6,5,4,3,9,8,0]
print(arrr(arr))