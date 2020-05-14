def jump(nums):
    stable=len(nums)-1
    for i in range(len(nums)-1,-1,-1):
        if nums[i]+i>=stable:
            stable=i
            
    return stable==0

l=[3,2,1,0,4]
print(jump(l))