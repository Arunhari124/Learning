def arrr(arr):
    t=10
    nums=set()
    for i in range(len(arr)):
        num=arr[i]
        match=t-num
        if  match in nums:
            return num,match
        else:
            nums.add(num)

arr=[6,5,4,3,9,8,0]

print(arrr(arr))